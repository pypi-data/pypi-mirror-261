import logging
from typing import Any, Iterable, Optional, Sequence

from aiokafka import ConsumerRecord
from typing_extensions import override

from faststream.broker.core.mixins import LoggingMixin
from faststream.broker.message import StreamMessage
from faststream.log import access_logger
from faststream.types import AnyDict


class KafkaLoggingMixin(LoggingMixin):
    """A class that provides logging functionality for Kafka.

    Attributes:
        _max_topic_len : maximum length of the topic name

    Methods:
        __init__ : initializes the KafkaLoggingMixin object
        _get_log_context : returns the log context for a given message and topics
        fmt : returns the log format string
        _setup_log_context : sets up the log context for a given list of topics

    """

    _max_topic_len: int

    def __init__(
        self,
        *args: Any,
        logger: Optional[logging.Logger] = access_logger,
        log_level: int = logging.INFO,
        log_fmt: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the class.

        Args:
            *args: Variable length argument list
            logger: Optional logger object
            log_level: Log level (default: logging.INFO)
            log_fmt: Optional log format string
            **kwargs: Arbitrary keyword arguments

        Returns:
            None

        """
        super().__init__(
            *args,
            logger=logger,
            log_level=log_level,
            log_fmt=log_fmt,
            **kwargs,
        )
        self._max_topic_len = 4
        self._max_group_len = 0

    @override
    def _get_log_context(  # type: ignore[override]
        self,
        message: Optional[StreamMessage[ConsumerRecord]],
        topics: Sequence[str] = (),
        group_id: Optional[str] = None,
    ) -> AnyDict:
        """Get the log context.

        Args:
            message: Optional stream message of type ConsumerRecord
            topics: Sequence of topics
            group_id: Optional group ID

        Returns:
            A dictionary containing the log context

        """
        if topics:
            topic = ", ".join(topics)
        elif message is not None:
            topic = message.raw_message.topic
        else:
            topic = ""

        context = {
            "topic": topic,
            "group_id": group_id or "",
            **super()._get_log_context(message),
        }
        return context

    @property
    def fmt(self) -> str:
        return super().fmt or (
            "%(asctime)s %(levelname)s - "
            + f"%(topic)-{self._max_topic_len}s | "
            + (f"%(group_id)-{self._max_group_len}s | " if self._max_group_len else "")
            + f"%(message_id)-{self._message_id_ln}s "
            + "- %(message)s"
        )

    def _setup_log_context(
        self, topics: Iterable[str], group_id: Optional[str] = None
    ) -> None:
        """Set up log context.

        Args:
            topics: An iterable of topics.
            group_id: Optional group ID.

        Returns:
            None.

        """
        for t in topics:
            self._max_topic_len = max((self._max_topic_len, len(t)))

        if group_id:
            self._max_group_len = max((self._max_group_len, len(group_id)))
