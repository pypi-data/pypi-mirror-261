import warnings
from abc import abstractmethod
from contextlib import ExitStack, asynccontextmanager
from functools import partial
from types import MethodType, TracebackType
from typing import Any, AsyncGenerator, Dict, Generic, Optional, Type, TypeVar
from unittest.mock import AsyncMock, MagicMock

from anyio.from_thread import start_blocking_portal

from faststream.app import FastStream
from faststream.broker.core.abc import BrokerUsecase
from faststream.broker.core.asynchronous import BrokerAsyncUsecase
from faststream.broker.handler import AsyncHandler
from faststream.broker.middlewares import CriticalLogMiddleware
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.types import SendableMessage, SettingField
from faststream.utils.ast import is_contains_context_name
from faststream.utils.functions import timeout_scope

Broker = TypeVar("Broker", bound=BrokerAsyncUsecase[Any, Any])


class TestApp:
    """A class to represent a test application.

    Attributes:
        app : an instance of FastStream
        _extra_options : optional dictionary of additional options
        _event : an instance of anyio.Event
        _task : an instance of TaskGroup

    Methods:
        __init__ : initializes the TestApp object
        __aenter__ : enters the asynchronous context and starts the FastStream application
        __aexit__ : exits the asynchronous context and stops the FastStream application

    """

    __test__ = False

    app: FastStream
    _extra_options: Dict[str, SettingField]

    def __init__(
        self,
        app: FastStream,
        run_extra_options: Optional[Dict[str, SettingField]] = None,
    ) -> None:
        """Initialize a class instance.

        Args:
            app: An instance of the FastStream class.
            run_extra_options: Optional dictionary of extra options for running the application.

        Returns:
            None

        """
        self.app = app
        self._extra_options = run_extra_options or {}

    def __enter__(self) -> FastStream:
        with ExitStack() as stack:
            portal = stack.enter_context(start_blocking_portal())

            lifespan_context = self.app.lifespan_context(**self._extra_options)
            stack.enter_context(portal.wrap_async_context_manager(lifespan_context))
            portal.call(partial(self.app._start, run_extra_options=self._extra_options))

            @stack.callback
            def wait_shutdown() -> None:
                portal.call(self.app._shutdown)

            self.exit_stack = stack.pop_all()

        return self.app

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        self.exit_stack.close()

    async def __aenter__(self) -> FastStream:
        self.lifespan_scope = self.app.lifespan_context(**self._extra_options)
        await self.lifespan_scope.__aenter__()
        await self.app._start(run_extra_options=self._extra_options)
        return self.app

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        """Exit the asynchronous context manager.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The exception instance raised, if any.
            exec_tb: The traceback for the exception raised, if any.

        Returns:
            None
        """
        await self.app._shutdown()
        await self.lifespan_scope.__aexit__(exc_type, exc_val, exec_tb)


class TestBroker(Generic[Broker]):
    """A class to represent a test broker."""

    # This is set so pytest ignores this class
    __test__ = False

    def __init__(
        self,
        broker: Broker,
        with_real: bool = False,
        connect_only: Optional[bool] = None,
    ) -> None:
        """Initialize a class instance.

        Args:
            broker: An instance of the Broker class.
            with_real: Whether to use a real broker.
            connect_only: Whether to only connect to the broker.

        """
        self.with_real = with_real
        self.broker = broker

        if connect_only is None:
            try:
                connect_only = is_contains_context_name(
                    self.__class__.__name__,
                    TestApp.__name__,
                )

            except Exception as e:  # pragma: no cover
                # TODO: remove with 0.5.0
                warnings.warn(
                    (
                        f"\nError `{e!r}` occurred at `{self.__class__.__name__}` AST parsing"
                        "\nPlease, report us by creating an Issue with your TestClient use case"
                        "\nhttps://github.com/airtai/faststream/issues/new?labels=bug&template=bug_report.md&title=Bug:%20TestClient%20AST%20parsing"
                    ),
                    category=RuntimeWarning,
                    stacklevel=1,
                )

                connect_only = False

        self.connect_only = connect_only

    async def __aenter__(self) -> Broker:
        self._ctx = self._create_ctx()
        return await self._ctx.__aenter__()

    async def __aexit__(self, *args: Any) -> None:
        await self._ctx.__aexit__(*args)

    @asynccontextmanager
    async def _create_ctx(self) -> AsyncGenerator[Broker, None]:
        if not self.with_real:
            self._patch_test_broker(self.broker)
        else:
            self._fake_start(self.broker)

        async with self.broker:
            try:
                if not self.connect_only:
                    await self.broker.start()
                yield self.broker
            finally:
                self._fake_close(self.broker)

    @classmethod
    def _patch_test_broker(cls, broker: Broker) -> None:
        broker.start = AsyncMock(wraps=partial(cls._fake_start, broker))  # type: ignore[method-assign]
        broker._connect = MethodType(cls._fake_connect, broker)  # type: ignore[method-assign]
        broker.close = AsyncMock()  # type: ignore[method-assign]

    @classmethod
    def _fake_start(cls, broker: Broker, *args: Any, **kwargs: Any) -> None:
        patch_broker_calls(broker)

        for key, p in broker._publishers.items():
            if p._fake_handler:
                continue

            handler = broker.handlers.get(key)

            if handler is not None:
                mock = MagicMock()
                p.set_test(mock=mock, with_fake=False)
                for f, _, _, _, _, _ in handler.calls:
                    f.set_test()
                    assert f.mock  # nosec B101
                    f.mock.side_effect = mock

            else:
                f = cls.create_publisher_fake_subscriber(broker, p)
                f.set_test()
                assert f.mock  # nosec B101
                p.set_test(mock=f.mock, with_fake=True)

            cls.patch_publisher(broker, p)

        for handler in broker.handlers.values():
            handler.running = True

    @classmethod
    def _fake_close(
        cls,
        broker: Broker,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        broker.middlewares = [
            CriticalLogMiddleware(broker.logger, broker.log_level),
            *broker.middlewares,
        ]

        for p in broker._publishers.values():
            if p._fake_handler:
                p.reset_test()
                cls.remove_publisher_fake_subscriber(broker, p)

        for h in broker.handlers.values():
            h.running = False
            for f, _, _, _, _, _ in h.calls:
                f.reset_test()

    @staticmethod
    @abstractmethod
    def create_publisher_fake_subscriber(
        broker: Broker, publisher: Any
    ) -> HandlerCallWrapper[Any, Any, Any]:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def remove_publisher_fake_subscriber(broker: Broker, publisher: Any) -> None:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    async def _fake_connect(broker: Broker, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def patch_publisher(broker: Broker, publisher: Any) -> None:
        raise NotImplementedError()


def patch_broker_calls(broker: BrokerUsecase[Any, Any]) -> None:
    """Patch broker calls.

    Args:
        broker: The broker to patch.

    Returns:
        None.

    """
    broker.middlewares = tuple(
        filter(  # type: ignore[assignment]
            lambda x: not isinstance(x, CriticalLogMiddleware),
            broker.middlewares,
        )
    )
    broker._abc_start()

    for handler in broker.handlers.values():
        for f, _, _, _, _, _ in handler.calls:
            f.set_test()


async def call_handler(
    handler: AsyncHandler[Any],
    message: Any,
    rpc: bool = False,
    rpc_timeout: Optional[float] = 30.0,
    raise_timeout: bool = False,
) -> Optional[SendableMessage]:
    """Asynchronously call a handler function.

    Args:
        handler: The handler function to be called.
        message: The message to be passed to the handler function.
        rpc: Whether the call is a remote procedure call (RPC).
        rpc_timeout: The timeout for the RPC, in seconds.
        raise_timeout: Whether to raise a timeout error if the RPC times out.

    Returns:
        The result of the handler function if `rpc` is True, otherwise None.

    Raises:
        TimeoutError: If the RPC times out and `raise_timeout` is True.

    """
    with timeout_scope(rpc_timeout, raise_timeout):
        result = await handler.consume(message)

        if rpc is True:
            return result

    return None
