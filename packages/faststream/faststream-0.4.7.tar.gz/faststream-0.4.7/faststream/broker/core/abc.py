import logging
import warnings
from abc import ABC, abstractmethod
from functools import partial
from itertools import chain
from types import TracebackType
from typing import (
    Any,
    AsyncContextManager,
    Awaitable,
    Callable,
    Generic,
    List,
    Mapping,
    Optional,
    Sequence,
    Sized,
    Tuple,
    Type,
    Union,
    cast,
)

from fast_depends._compat import PYDANTIC_V2
from fast_depends.core import CallModel, build_call_model
from fast_depends.dependencies import Depends
from pydantic import Field, create_model

from faststream._compat import PydanticUndefined, is_test_env
from faststream.asyncapi import schema as asyncapi
from faststream.broker.core.mixins import LoggingMixin
from faststream.broker.handler import BaseHandler
from faststream.broker.message import StreamMessage
from faststream.broker.middlewares import BaseMiddleware, CriticalLogMiddleware
from faststream.broker.publisher import BasePublisher
from faststream.broker.push_back_watcher import WatcherContext
from faststream.broker.router import BrokerRouter
from faststream.broker.types import (
    ConnectionType,
    CustomDecoder,
    CustomParser,
    Filter,
    MsgType,
    P_HandlerParams,
    T_HandlerReturn,
    WrappedReturn,
)
from faststream.broker.utils import (
    change_logger_handlers,
    get_watcher,
    set_message_context,
)
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.log import access_logger
from faststream.security import BaseSecurity
from faststream.types import AnyDict, F_Return, F_Spec
from faststream.utils import apply_types, context
from faststream.utils.functions import (
    fake_context,
    get_function_positional_arguments,
    to_async,
)


class BrokerUsecase(
    ABC,
    Generic[MsgType, ConnectionType],
    LoggingMixin,
):
    """A class representing a broker use case.

    Attributes:
        logger : optional logger object
        log_level : log level
        handlers : dictionary of handlers
        _publishers : dictionary of publishers
        dependencies : sequence of dependencies
        started : boolean indicating if the broker has started
        middlewares : sequence of middleware functions
        _global_parser : optional custom parser object
        _global_decoder : optional custom decoder object
        _connection : optional connection object
        _fmt : optional string format

    Methods:
        __init__ : constructor method
        include_router : include a router in the broker
        include_routers : include multiple routers in the broker
        _resolve_connection_kwargs : resolve connection kwargs
        _wrap_handler : wrap a handler function
        _abc_start : start the broker
        _abc_close : close the broker
        _abc__close : close the broker connection
        _process_message : process a message
        subscriber : decorator to register a subscriber
        publisher : register a publisher
        _wrap_decode_message : wrap a message decoding function

    """

    logger: Optional[logging.Logger]
    log_level: int
    handlers: Mapping[Any, BaseHandler[MsgType]]
    _publishers: Mapping[Any, BasePublisher[MsgType]]

    dependencies: Sequence[Depends]
    started: bool
    middlewares: Sequence[Callable[[Any], BaseMiddleware]]
    _global_parser: Optional[CustomParser[MsgType, StreamMessage[MsgType]]]
    _global_decoder: Optional[CustomDecoder[StreamMessage[MsgType]]]
    _connection: Optional[ConnectionType]
    _fmt: Optional[str]

    def __init__(
        self,
        url: Union[str, List[str]],
        *args: Any,
        # AsyncAPI kwargs
        protocol: Optional[str] = None,
        protocol_version: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[Sequence[Union[asyncapi.Tag, asyncapi.TagDict]]] = None,
        asyncapi_url: Union[str, List[str], None] = None,
        # broker kwargs
        apply_types: bool = True,
        validate: bool = True,
        logger: Optional[logging.Logger] = access_logger,
        log_level: int = logging.INFO,
        log_fmt: Optional[str] = "%(asctime)s %(levelname)s - %(message)s",
        dependencies: Sequence[Depends] = (),
        middlewares: Optional[Sequence[Callable[[MsgType], BaseMiddleware]]] = None,
        decoder: Optional[CustomDecoder[StreamMessage[MsgType]]] = None,
        parser: Optional[CustomParser[MsgType, StreamMessage[MsgType]]] = None,
        security: Optional[BaseSecurity] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize a broker.

        Args:
            url: The URL or list of URLs to connect to.
            *args: Additional arguments.
            protocol: The protocol to use for the connection.
            protocol_version: The version of the protocol.
            description: A description of the broker.
            tags: Tags associated with the broker.
            asyncapi_url: The URL or list of URLs to the AsyncAPI schema.
            apply_types: Whether to apply types to messages.
            validate: Whether to cast types using Pydantic validation.
            logger: The logger to use.
            log_level: The log level to use.
            log_fmt: The log format to use.
            dependencies: Dependencies of the broker.
            middlewares: Middlewares to use.
            decoder: Custom decoder for messages.
            parser: Custom parser for messages.
            security: Security scheme to use.
            **kwargs: Additional keyword arguments.

        """
        super().__init__(
            logger=logger,
            log_level=log_level,
            log_fmt=log_fmt,
        )

        self._connection = None
        self._is_apply_types = apply_types
        self._is_validate = validate
        self.handlers = {}
        self._publishers = {}
        empty_middleware: Sequence[Callable[[MsgType], BaseMiddleware]] = ()
        midd_args: Sequence[Callable[[MsgType], BaseMiddleware]] = (
            middlewares or empty_middleware
        )
        self.middlewares = [CriticalLogMiddleware(logger, log_level), *midd_args]
        self.dependencies = dependencies

        self._connection_args = (url, *args)
        self._connection_kwargs = kwargs

        self._global_parser = parser
        self._global_decoder = decoder

        context.set_global("logger", logger)
        context.set_global("broker", self)

        self.started = False

        # AsyncAPI information
        self.url = asyncapi_url or url
        self.protocol = protocol
        self.protocol_version = protocol_version
        self.description = description
        self.tags = tags
        self.security = security

    def include_router(self, router: BrokerRouter[Any, MsgType]) -> None:
        """Includes a router in the current object.

        Args:
            router: The router to be included.

        Returns:
            None

        """
        for r in router._handlers:
            self.subscriber(*r.args, **r.kwargs)(r.call)

        self._publishers = {**self._publishers, **router._publishers}

    def include_routers(self, *routers: BrokerRouter[Any, MsgType]) -> None:
        """Includes routers in the current object.

        Args:
            *routers: Variable length argument list of routers to include.

        Returns:
            None

        """
        for r in routers:
            self.include_router(r)

    def _resolve_connection_kwargs(self, *args: Any, **kwargs: Any) -> AnyDict:
        """Resolve connection keyword arguments.

        Args:
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.

        Returns:
            A dictionary containing the resolved connection keyword arguments.

        """
        arguments = get_function_positional_arguments(self.__init__)  # type: ignore
        init_kwargs = {
            **self._connection_kwargs,
            **dict(zip(arguments, self._connection_args)),
        }

        connect_kwargs = {
            **kwargs,
            **dict(zip(arguments, args)),
        }
        return {**init_kwargs, **connect_kwargs}

    def _wrap_handler(
        self,
        func: Union[
            HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
            Callable[P_HandlerParams, T_HandlerReturn],
        ],
        *,
        retry: Union[bool, int] = False,
        extra_dependencies: Sequence[Depends] = (),
        no_ack: bool = False,
        _raw: bool = False,
        _get_dependant: Optional[Any] = None,
        _process_kwargs: Optional[AnyDict] = None,
    ) -> Tuple[
        HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
        CallModel[Any, Any],
    ]:
        """Wrap a handler function.

        Args:
            func: The handler function to wrap.
            retry: Whether to retry the handler function if it fails. Can be a boolean or an integer specifying the number of retries.
            extra_dependencies: Additional dependencies for the handler function.
            no_ack: Whether not to ack/nack/reject messages.
            _raw: Whether to use the raw handler function.
            _get_dependant: The dependant function to use.
            **broker_log_context_kwargs: Additional keyword arguments for the broker log context.

        Returns:
            A tuple containing the wrapped handler function and the call model.

        Raises:
            NotImplementedError: If silent animals are not supported.

        """
        build_dep = cast(
            Callable[[Callable[F_Spec, F_Return]], CallModel[F_Spec, F_Return]],
            _get_dependant or partial(build_call_model, cast=self._is_validate),
        )

        if isinstance(func, HandlerCallWrapper):
            handler_call, func = func, func._original_call
            if handler_call._wrapped_call is not None:
                return handler_call, build_dep(func)
        else:
            handler_call = HandlerCallWrapper(func)

        f = to_async(func)

        dependant = build_dep(f)

        extra = [
            build_dep(d.dependency)
            for d in chain(extra_dependencies, self.dependencies)
        ]

        extend_dependencies(extra, dependant)

        if getattr(dependant, "flat_params", None) is None:  # handle FastAPI Dependant
            dependant = _patch_fastapi_dependant(dependant)

        if self._is_apply_types and not _raw:
            f = apply_types(None, cast=self._is_validate)(f, dependant)  # type: ignore[arg-type,assignment]

        decode_f = self._wrap_decode_message(
            func=f,
            _raw=_raw,
            params=set(
                chain(
                    dependant.flat_params.keys(), *(d.flat_params.keys() for d in extra)
                )
            ),
        )

        process_f = self._process_message(
            func=decode_f,
            watcher=(
                partial(WatcherContext, watcher=get_watcher(self.logger, retry))  # type: ignore[arg-type]
                if not no_ack
                else fake_context
            ),
            **(_process_kwargs or {}),
        )

        process_f = set_message_context(process_f)

        handler_call.set_wrapped(process_f)
        return handler_call, dependant

    def _abc_start(self) -> None:
        if not self.started:
            self.started = True

            for h in self.handlers.values():
                h.global_middlewares = (*self.middlewares, *h.global_middlewares)

            if self.logger is not None:
                change_logger_handlers(self.logger, self.fmt)

    def _abc_close(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        """Closes the ABC.

        Args:
            exc_type: The exception type
            exc_val: The exception value
            exec_tb: The traceback

        Returns:
            None

        """
        self.started = False

    def _abc__close(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        """Closes the connection.

        Args:
            exc_type: The type of the exception being handled (optional)
            exc_val: The exception instance being handled (optional)
            exec_tb: The traceback for the exception being handled (optional)

        Returns:
            None

        Note:
            This is an abstract method and must be implemented by subclasses.

        """
        self._connection = None

    @abstractmethod
    def _process_message(
        self,
        func: Callable[[StreamMessage[MsgType]], Awaitable[T_HandlerReturn]],
        watcher: Callable[..., AsyncContextManager[None]],
        **kwargs: Any,
    ) -> Callable[[StreamMessage[MsgType]], Awaitable[WrappedReturn[T_HandlerReturn]]]:
        """Processes a message using a given function and watcher.

        Args:
            func: A callable that takes a StreamMessage of type MsgType and returns an Awaitable of type T_HandlerReturn.
            watcher: An instance of BaseWatcher.
            disable_watcher: Whether to use watcher context.
            kwargs: Additional keyword arguments.

        Returns:
            A callable that takes a StreamMessage of type MsgType and returns an Awaitable of type WrappedReturn[T_HandlerReturn].

        Raises:
            NotImplementedError: If the method is not implemented.

        """
        raise NotImplementedError()

    @abstractmethod
    def subscriber(  # type: ignore[return]
        self,
        *broker_args: Any,
        retry: Union[bool, int] = False,
        dependencies: Sequence[Depends] = (),
        decoder: Optional[CustomDecoder[StreamMessage[MsgType]]] = None,
        parser: Optional[CustomParser[MsgType, StreamMessage[MsgType]]] = None,
        middlewares: Optional[
            Sequence[
                Callable[
                    [StreamMessage[MsgType]],
                    BaseMiddleware,
                ]
            ]
        ] = None,
        filter: Filter[StreamMessage[MsgType]] = lambda m: not m.processed,
        _raw: bool = False,
        _get_dependant: Optional[Any] = None,
        **broker_kwargs: Any,
    ) -> Callable[
        [
            Union[
                Callable[P_HandlerParams, T_HandlerReturn],
                HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
            ]
        ],
        HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
    ]:
        """This is a function decorator for subscribing to a message broker.

        Args:
            *broker_args: Positional arguments to be passed to the broker.
            retry: Whether to retry the subscription if it fails. Can be a boolean or an integer specifying the number of retries.
            dependencies: Sequence of dependencies to be injected into the handler function.
            decoder: Custom decoder function to decode the message.
            parser: Custom parser function to parse the decoded message.
            middlewares: Sequence of middleware functions to be applied to the message.
            filter: Filter function to filter the messages to be processed.
            _raw: Whether to return the raw message instead of the processed message.
            _get_dependant: Optional parameter to get the dependant object.
            **broker_kwargs: Keyword arguments to be passed to the broker.

        Returns:
            A callable object that can be used as a decorator for a handler function.

        Raises:
            RuntimeWarning: If the broker is already running.

        """
        if self.started and not is_test_env():  # pragma: no cover
            warnings.warn(
                "You are trying to register `handler` with already running broker\n"
                "It has no effect until broker restarting.",
                category=RuntimeWarning,
                stacklevel=1,
            )

    @abstractmethod
    def publisher(
        self,
        key: Any,
        publisher: BasePublisher[MsgType],
    ) -> BasePublisher[MsgType]:
        """Publishes a publisher.

        Args:
            key: The key associated with the publisher.
            publisher: The publisher to be published.

        Returns:
            The published publisher.

        Raises:
            NotImplementedError: If the method is not implemented.

        """
        self._publishers = {**self._publishers, key: publisher}
        return publisher

    @abstractmethod
    def _wrap_decode_message(
        self,
        func: Callable[..., Awaitable[T_HandlerReturn]],
        params: Sized = (),
        _raw: bool = False,
    ) -> Callable[[StreamMessage[MsgType]], Awaitable[T_HandlerReturn]]:
        """Wrap a decoding message function.

        Args:
            func: The function to wrap.
            params: The parameters to pass to the function.
            _raw: Whether to return the raw message or not.

        Returns:
            The wrapped function.

        Raises:
            NotImplementedError: If the method is not implemented.

        """
        raise NotImplementedError()


def extend_dependencies(
    extra: Sequence[CallModel[Any, Any]], dependant: CallModel[Any, Any]
) -> CallModel[Any, Any]:
    """Extends the dependencies of a function or FastAPI dependency.

    Args:
        extra: Additional dependencies to be added.
        dependant: The function or FastAPI dependency whose dependencies will be extended.

    Returns:
        The updated function or FastAPI dependency.

    """
    if isinstance(dependant, CallModel):
        dependant.extra_dependencies = (*dependant.extra_dependencies, *extra)
    else:  # FastAPI dependencies
        dependant.dependencies.extend(extra)
    return dependant


def _patch_fastapi_dependant(
    dependant: CallModel[P_HandlerParams, Awaitable[T_HandlerReturn]],
) -> CallModel[P_HandlerParams, Awaitable[T_HandlerReturn]]:
    """Patch FastAPI dependant.

    Args:
        dependant: The dependant to be patched.

    Returns:
        The patched dependant.

    """
    params = dependant.query_params + dependant.body_params  # type: ignore[attr-defined]

    for d in dependant.dependencies:
        params.extend(d.query_params + d.body_params)  # type: ignore[attr-defined]

    params_unique = {}
    for p in params:
        if p.name not in params_unique:
            info = p.field_info if PYDANTIC_V2 else p

            field_data = {
                "default": ... if info.default is PydanticUndefined else info.default,
                "default_factory": info.default_factory,
                "alias": info.alias,
            }

            if PYDANTIC_V2:
                from pydantic.fields import FieldInfo

                info = cast(FieldInfo, info)

                field_data.update(
                    {
                        "title": info.title,
                        "alias_priority": info.alias_priority,
                        "validation_alias": info.validation_alias,
                        "serialization_alias": info.serialization_alias,
                        "description": info.description,
                        "discriminator": info.discriminator,
                        "examples": info.examples,
                        "exclude": info.exclude,
                        "json_schema_extra": info.json_schema_extra,
                    }
                )

                f = next(
                    filter(
                        lambda x: isinstance(x, FieldInfo),
                        p.field_info.metadata or (),
                    ),
                    Field(**field_data),  # type: ignore[pydantic-field]
                )

            else:
                from pydantic.fields import ModelField  # type: ignore[attr-defined]

                info = cast(ModelField, info)

                field_data.update(
                    {
                        "title": info.field_info.title,
                        "description": info.field_info.description,
                        "discriminator": info.field_info.discriminator,
                        "exclude": info.field_info.exclude,
                        "gt": info.field_info.gt,
                        "ge": info.field_info.ge,
                        "lt": info.field_info.lt,
                        "le": info.field_info.le,
                    }
                )
                f = Field(**field_data)  # type: ignore[pydantic-field]

            params_unique[p.name] = (
                info.annotation,
                f,
            )

    dependant.model = create_model(
        getattr(dependant.call, "__name__", type(dependant.call).__name__)
    )

    dependant.custom_fields = {}
    dependant.flat_params = params_unique  # type: ignore[assignment,misc]

    return dependant
