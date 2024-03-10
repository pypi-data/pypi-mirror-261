from typing import Dict, Optional

from faststream.asyncapi.schema import (
    Channel,
    ChannelBinding,
    CorrelationId,
    Message,
    Operation,
    OperationBinding,
)
from faststream.asyncapi.schema.bindings import amqp
from faststream.asyncapi.utils import resolve_payloads
from faststream.rabbit.handler import LogicHandler
from faststream.rabbit.publisher import LogicPublisher
from faststream.rabbit.shared.constants import ExchangeType
from faststream.rabbit.shared.schemas import RabbitExchange


class Publisher(LogicPublisher):
    """A class representing a publisher.

    Attributes:
        name : name of the publisher

    Methods:
        get_payloads : Get the payloads for the publisher

    """

    @property
    def name(self) -> str:
        routing = (
            self.routing_key
            or (self.queue.routing if _is_exchange(self.exchange) else None)
            or "_"
        )
        return (
            self.title or f"{routing}:{getattr(self.exchange, 'name', '_')}:Publisher"
        )

    def schema(self) -> Dict[str, Channel]:
        if not self.include_in_schema:
            return {}

        payloads = self.get_payloads()

        return {
            self.name: Channel(
                description=self.description,  # type: ignore[attr-defined]
                publish=Operation(
                    bindings=OperationBinding(
                        amqp=amqp.OperationBinding(
                            cc=self.routing or None,
                            deliveryMode=2 if self.persist else 1,
                            mandatory=self.mandatory,
                            replyTo=self.reply_to,
                            priority=self.priority,
                        ),
                    )
                    if _is_exchange(self.exchange)
                    else None,
                    message=Message(
                        title=f"{self.name}:Message",
                        payload=resolve_payloads(
                            payloads,
                            "Publisher",
                            served_words=2 if self.title is None else 1,
                        ),
                        correlationId=CorrelationId(
                            location="$message.header#/correlation_id"
                        ),
                    ),
                ),
                bindings=ChannelBinding(
                    amqp=amqp.ChannelBinding(
                        **{
                            "is": "routingKey",  # type: ignore
                            "queue": amqp.Queue(
                                name=self.queue.name,
                                durable=self.queue.durable,
                                exclusive=self.queue.exclusive,
                                autoDelete=self.queue.auto_delete,
                                vhost=self.virtual_host,
                            )
                            if _is_exchange(self.exchange) and self.queue.name
                            else None,
                            "exchange": (
                                amqp.Exchange(type="default", vhost=self.virtual_host)
                                if self.exchange is None
                                else amqp.Exchange(
                                    type=self.exchange.type,  # type: ignore
                                    name=self.exchange.name,
                                    durable=self.exchange.durable,
                                    autoDelete=self.exchange.auto_delete,
                                    vhost=self.virtual_host,
                                )
                            ),
                        }
                    )
                ),
            )
        }


class Handler(LogicHandler):
    """A class that serves as a handler for RMQAsyncAPIChannel and LogicHandler.

    Methods:
        - name(): Returns the name of the handler.
        - get_payloads(): Returns a list of payloads.

    """

    def schema(self) -> Dict[str, Channel]:
        if not self.include_in_schema:
            return {}

        payloads = self.get_payloads()

        handler_name = (
            self._title
            or f"{self.queue.name}:{getattr(self.exchange, 'name', '_')}:{self.call_name}"
        )

        return {
            handler_name: Channel(
                description=self.description,  # type: ignore[attr-defined]
                subscribe=Operation(
                    bindings=OperationBinding(
                        amqp=amqp.OperationBinding(
                            cc=self.queue.routing,
                        ),
                    )
                    if _is_exchange(self.exchange)
                    else None,
                    message=Message(
                        title=f"{handler_name}:Message",
                        payload=resolve_payloads(payloads),
                        correlationId=CorrelationId(
                            location="$message.header#/correlation_id"
                        ),
                    ),
                ),
                bindings=ChannelBinding(
                    amqp=amqp.ChannelBinding(
                        **{
                            "is": "routingKey",  # type: ignore
                            "queue": amqp.Queue(
                                name=self.queue.name,
                                durable=self.queue.durable,
                                exclusive=self.queue.exclusive,
                                autoDelete=self.queue.auto_delete,
                                vhost=self.virtual_host,
                            )
                            if _is_exchange(self.exchange)
                            else None,
                            "exchange": (
                                amqp.Exchange(type="default", vhost=self.virtual_host)
                                if self.exchange is None
                                else amqp.Exchange(
                                    type=self.exchange.type,  # type: ignore
                                    name=self.exchange.name,
                                    durable=self.exchange.durable,
                                    autoDelete=self.exchange.auto_delete,
                                    vhost=self.virtual_host,
                                )
                            ),
                        }
                    )
                ),
            )
        }


def _is_exchange(exchange: Optional[RabbitExchange]) -> bool:
    """Check if an exchange is a valid exchange type.

    Args:
        exchange: The exchange to check

    Returns:
        True if the exchange is a valid exchange type, False otherwise

    """
    if exchange and exchange.type in (
        ExchangeType.FANOUT.value,
        ExchangeType.HEADERS.value,
    ):
        return False
    return True
