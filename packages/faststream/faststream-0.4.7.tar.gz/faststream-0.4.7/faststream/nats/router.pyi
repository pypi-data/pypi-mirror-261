from typing import Any, Callable, Sequence

from fast_depends.dependencies import Depends
from nats.aio.msg import Msg
from nats.js import api
from typing_extensions import override

from faststream.broker.core.asynchronous import default_filter
from faststream.broker.middlewares import BaseMiddleware
from faststream.broker.types import (
    CustomDecoder,
    CustomParser,
    Filter,
    P_HandlerParams,
    T_HandlerReturn,
)
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.nats.asyncapi import Publisher
from faststream.nats.js_stream import JStream
from faststream.nats.message import NatsMessage
from faststream.nats.pull_sub import PullSub
from faststream.nats.shared.router import NatsRoute
from faststream.nats.shared.router import NatsRouter as BaseRouter

class NatsRouter(BaseRouter):
    _publishers: dict[str, Publisher]  # type: ignore[assignment]

    def __init__(
        self,
        prefix: str = "",
        handlers: Sequence[NatsRoute] = (),
        *,
        dependencies: Sequence[Depends] = (),
        middlewares: Sequence[Callable[[Msg], BaseMiddleware]] | None = None,
        parser: CustomParser[Msg, NatsMessage] | None = None,
        decoder: CustomDecoder[NatsMessage] | None = None,
        include_in_schema: bool = True,
    ) -> None: ...
    @override
    @staticmethod
    def _get_publisher_key(publisher: Publisher) -> str: ...  # type: ignore[override]
    @override
    @staticmethod
    def _update_publisher_prefix(  # type: ignore[override]
        prefix: str,
        publisher: Publisher,
    ) -> Publisher: ...
    @override
    def publisher(  # type: ignore[override]
        self,
        subject: str,
        headers: dict[str, str] | None = None,
        reply_to: str = "",
        # AsyncAPI information
        title: str | None = None,
        description: str | None = None,
        schema: Any | None = None,
        include_in_schema: bool = True,
    ) -> Publisher: ...
    @override
    def subscriber(  # type: ignore[override]
        self,
        subject: str,
        queue: str = "",
        pending_msgs_limit: int | None = None,
        pending_bytes_limit: int | None = None,
        # Core arguments
        max_msgs: int = 0,
        ack_first: bool = False,
        # JS arguments
        stream: str | JStream | None = None,
        durable: str | None = None,
        config: api.ConsumerConfig | None = None,
        ordered_consumer: bool = False,
        idle_heartbeat: float | None = None,
        flow_control: bool = False,
        deliver_policy: api.DeliverPolicy | None = None,
        headers_only: bool | None = None,
        # pull arguments
        pull_sub: PullSub | None = None,
        inbox_prefix: bytes = api.INBOX_PREFIX,
        # broker arguments
        dependencies: Sequence[Depends] = (),
        parser: CustomParser[Msg, NatsMessage] | None = None,
        decoder: CustomDecoder[NatsMessage] | None = None,
        middlewares: Sequence[Callable[[Msg], BaseMiddleware]] | None = None,
        filter: Filter[NatsMessage] = default_filter,
        retry: bool = False,
        no_ack: bool = False,
        # AsyncAPI information
        title: str | None = None,
        description: str | None = None,
        include_in_schema: bool = True,
        **__service_kwargs: Any,
    ) -> Callable[
        [Callable[P_HandlerParams, T_HandlerReturn]],
        HandlerCallWrapper[Msg, P_HandlerParams, T_HandlerReturn],
    ]: ...
