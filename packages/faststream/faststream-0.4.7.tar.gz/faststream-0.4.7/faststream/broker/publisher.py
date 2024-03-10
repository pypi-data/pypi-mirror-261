from abc import abstractmethod
from dataclasses import dataclass, field
from inspect import unwrap
from typing import Any, Callable, Generic, List, Optional, Tuple
from unittest.mock import MagicMock

from fast_depends._compat import create_model, get_config_base
from fast_depends.core import CallModel, build_call_model

from faststream.asyncapi.base import AsyncAPIOperation
from faststream.asyncapi.message import get_response_schema
from faststream.asyncapi.utils import to_camelcase
from faststream.broker.types import MsgType, P_HandlerParams, T_HandlerReturn
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.types import AnyDict, SendableMessage


@dataclass
class BasePublisher(AsyncAPIOperation, Generic[MsgType]):
    """A base class for publishers in an asynchronous API.

    Attributes:
        title : optional title of the publisher
        _description : optional description of the publisher
        _fake_handler : boolean indicating if a fake handler is used
        calls : list of callable objects
        mock : MagicMock object for mocking purposes

    Methods:
        description() : returns the description of the publisher
        __call__(func) : decorator to register a function as a handler for the publisher
        publish(message, correlation_id, **kwargs) : publishes a message with optional correlation ID

    Raises:
        NotImplementedError: if the publish method is not implemented.

    """

    title: Optional[str] = field(default=None)
    _description: Optional[str] = field(default=None)
    _schema: Optional[Any] = field(default=None)

    calls: List[Callable[..., Any]] = field(
        init=False, default_factory=list, repr=False
    )
    _fake_handler: bool = field(default=False, repr=False)
    mock: Optional[MagicMock] = field(init=False, default=None, repr=False)

    @property
    def description(self) -> Optional[str]:
        return self._description

    def set_test(
        self,
        mock: MagicMock,
        with_fake: bool,
    ) -> None:
        self.mock = mock
        self._fake_handler = with_fake

    def reset_test(self) -> None:
        self._fake_handler = False
        self.mock = None

    def __call__(
        self,
        func: Callable[P_HandlerParams, T_HandlerReturn],
    ) -> HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn]:
        """This is a Python function.

        Args:
            func: A callable object that takes `P_HandlerParams` as input and returns `T_HandlerReturn`.

        Returns:
            An instance of `HandlerCallWrapper` class.

        Raises:
            TypeError: If `func` is not callable.

        """
        handler_call: HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn] = (
            HandlerCallWrapper(func)
        )
        handler_call._publishers.append(self)
        self.calls.append(handler_call._original_call)
        return handler_call

    @abstractmethod
    async def publish(
        self,
        message: SendableMessage,
        correlation_id: Optional[str] = None,
        **kwargs: Any,
    ) -> Optional[SendableMessage]:
        """Publish a message.

        Args:
            message: The message to be published.
            correlation_id: Optional correlation ID for the message.
            **kwargs: Additional keyword arguments.

        Returns:
            The published message.

        Raises:
            NotImplementedError: If the method is not implemented.

        """
        raise NotImplementedError()

    def get_payloads(self) -> List[Tuple[AnyDict, str]]:
        payloads: List[Tuple[AnyDict, str]] = []

        if self._schema:
            params = {"response__": (self._schema, ...)}

            call_model: CallModel[Any, Any] = CallModel(
                call=lambda: None,
                model=create_model("Fake"),
                response_model=create_model(  # type: ignore[call-overload]
                    "",
                    __config__=get_config_base(),  # type: ignore[arg-type]
                    **params,  # type: ignore[arg-type]
                ),
                params=params,
            )

            body = get_response_schema(
                call_model,
                prefix=f"{self.name}:Message",
            )
            if body:  # pragma: no branch
                payloads.append((body, ""))

        else:
            for call in self.calls:
                call_model = build_call_model(call)
                body = get_response_schema(
                    call_model,
                    prefix=f"{self.name}:Message",
                )
                if body:
                    payloads.append((body, to_camelcase(unwrap(call).__name__)))

        return payloads
