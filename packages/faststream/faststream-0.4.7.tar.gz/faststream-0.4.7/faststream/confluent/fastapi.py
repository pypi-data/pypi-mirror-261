from typing import Any, Callable

from confluent_kafka import Message
from typing_extensions import Annotated

from faststream.broker.fastapi.context import Context, ContextRepo, Logger
from faststream.broker.fastapi.router import StreamRouter
from faststream.broker.types import (
    P_HandlerParams,
    T_HandlerReturn,
)
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.confluent.broker import KafkaBroker as KB
from faststream.confluent.message import KafkaMessage as KM
from faststream.confluent.producer import AsyncConfluentFastProducer

__all__ = (
    "Context",
    "Logger",
    "ContextRepo",
    "KafkaRouter",
    "KafkaMessage",
    "KafkaBroker",
    "KafkaProducer",
)

KafkaMessage = Annotated[KM, Context("message")]
KafkaBroker = Annotated[KB, Context("broker")]
KafkaProducer = Annotated[AsyncConfluentFastProducer, Context("broker._producer")]


class KafkaRouter(StreamRouter[Message]):
    """A class to route Kafka streams.

    Attributes:
        broker_class : class representing the Kafka broker

    Methods:
        _setup_log_context : sets up the log context for the main broker and including broker
    """

    broker_class = KB

    def subscriber(
        self,
        *topics: str,
        **broker_kwargs: Any,
    ) -> Callable[
        [Callable[P_HandlerParams, T_HandlerReturn]],
        HandlerCallWrapper[Any, P_HandlerParams, T_HandlerReturn],
    ]:
        return super().subscriber(topics[0], *topics, **broker_kwargs)

    @staticmethod
    def _setup_log_context(
        main_broker: KB,
        including_broker: KB,
    ) -> None:
        """Set up log context for a Kafka broker.

        Args:
            main_broker: The main Kafka broker.
            including_broker: The Kafka broker to include in the log context.

        Returns:
            None
        """
        for h in including_broker.handlers.values():
            main_broker._setup_log_context(h.topics)
