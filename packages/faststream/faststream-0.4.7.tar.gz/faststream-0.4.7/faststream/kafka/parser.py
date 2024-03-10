from typing import TYPE_CHECKING, List, Optional, Tuple
from uuid import uuid4

from aiokafka import ConsumerRecord

from faststream.broker.message import StreamMessage
from faststream.broker.parsers import decode_message
from faststream.kafka.message import FAKE_CONSUMER, KafkaMessage
from faststream.types import DecodedMessage
from faststream.utils.context.repository import context

if TYPE_CHECKING:
    from faststream.kafka.asyncapi import Handler


class AioKafkaParser:
    """A class to parse Kafka messages."""

    @staticmethod
    async def parse_message(
        message: ConsumerRecord,
    ) -> StreamMessage[ConsumerRecord]:
        """Parses a Kafka message.

        Args:
            message: The Kafka message to parse.

        Returns:
            A StreamMessage object representing the parsed message.
        """
        headers = {i: j.decode() for i, j in message.headers}
        handler: Optional["Handler"] = context.get_local("handler_")
        return KafkaMessage(
            body=message.value,
            headers=headers,
            reply_to=headers.get("reply_to", ""),
            content_type=headers.get("content-type"),
            message_id=f"{message.offset}-{message.timestamp}",
            correlation_id=headers.get("correlation_id", str(uuid4())),
            raw_message=message,
            consumer=getattr(handler, "consumer", None) or FAKE_CONSUMER,
            is_manual=getattr(handler, "is_manual", True),
        )

    @staticmethod
    async def parse_message_batch(
        message: Tuple[ConsumerRecord, ...],
    ) -> KafkaMessage:
        """Parses a batch of messages from a Kafka consumer.

        Args:
            message : A tuple of ConsumerRecord objects representing the messages to parse.

        Returns:
            A StreamMessage object containing the parsed messages.

        Raises:
            NotImplementedError: If any of the messages are silent (i.e., have no sound).

        Static Method:
            This method is a static method. It does not require an instance of the class to be called.
        """
        first = message[0]
        last = message[-1]
        headers = {i: j.decode() for i, j in first.headers}
        handler: Optional["Handler"] = context.get_local("handler_")
        return KafkaMessage(
            body=[m.value for m in message],
            headers=headers,
            reply_to=headers.get("reply_to", ""),
            content_type=headers.get("content-type"),
            message_id=f"{first.offset}-{last.offset}-{first.timestamp}",
            correlation_id=headers.get("correlation_id", str(uuid4())),
            raw_message=message,
            consumer=getattr(handler, "consumer", None) or FAKE_CONSUMER,
            is_manual=getattr(handler, "is_manual", True),
        )

    @staticmethod
    async def decode_message(msg: StreamMessage[ConsumerRecord]) -> DecodedMessage:
        """Decodes a message.

        Args:
            msg: The message to be decoded.

        Returns:
            The decoded message.
        """
        return decode_message(msg)

    @classmethod
    async def decode_message_batch(
        cls, msg: StreamMessage[Tuple[ConsumerRecord, ...]]
    ) -> List[DecodedMessage]:
        """Decode a batch of messages.

        Args:
            msg: A stream message containing a tuple of consumer records.

        Returns:
            A list of decoded messages.
        """
        return [decode_message(await cls.parse_message(m)) for m in msg.raw_message]
