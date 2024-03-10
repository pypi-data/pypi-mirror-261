from dataclasses import dataclass, field
from typing import Any, Optional, Union

import aiormq
from aio_pika import IncomingMessage
from typing_extensions import override

from faststream.exceptions import NOT_CONNECTED_YET
from faststream.rabbit.producer import AioPikaFastProducer
from faststream.rabbit.shared.publisher import ABCPublisher
from faststream.rabbit.shared.schemas import get_routing_hash
from faststream.rabbit.types import AioPikaSendableMessage
from faststream.types import SendableMessage


@dataclass
class LogicPublisher(ABCPublisher[IncomingMessage]):
    """A class to publish messages for logic processing.

    Attributes:
        _producer : An optional AioPikaFastProducer object.

    Methods:
        publish : Publishes a message for logic processing.

    """

    _producer: Optional[AioPikaFastProducer] = field(default=None, init=False)

    @property
    def routing(self) -> Optional[str]:
        return self.routing_key or self.queue.routing

    def _get_routing_hash(self) -> int:
        return get_routing_hash(self.queue, self.exchange) + hash(self.routing_key)

    @override
    async def publish(  # type: ignore[override]
        self,
        message: AioPikaSendableMessage = "",
        *,
        rpc: bool = False,
        rpc_timeout: Optional[float] = 30.0,
        raise_timeout: bool = False,
        correlation_id: Optional[str] = None,
        priority: Optional[int] = None,
        **message_kwargs: Any,
    ) -> Union[aiormq.abc.ConfirmationFrameType, SendableMessage]:
        """Publish a message.

        Args:
            message: The message to be published.
            rpc: Whether the message is for RPC (Remote Procedure Call).
            rpc_timeout: Timeout for RPC.
            raise_timeout: Whether to raise an exception if timeout occurs.
            correlation_id: Correlation ID for the message.
            priority: Priority for the message.
            **message_kwargs: Additional keyword arguments for the message.

        Returns:
            ConfirmationFrameType or SendableMessage: The result of the publish operation.

        Raises:
            AssertionError: If `_producer` is not set up.

        """
        assert self._producer, NOT_CONNECTED_YET  # nosec B101
        return await self._producer.publish(
            message=message,
            exchange=self.exchange,
            routing_key=self.routing,
            mandatory=self.mandatory,
            immediate=self.immediate,
            timeout=self.timeout,
            rpc=rpc,
            rpc_timeout=rpc_timeout,
            raise_timeout=raise_timeout,
            persist=self.persist,
            reply_to=self.reply_to,
            correlation_id=correlation_id,
            priority=priority or self.priority,
            **self.message_kwargs,
            **message_kwargs,
        )
