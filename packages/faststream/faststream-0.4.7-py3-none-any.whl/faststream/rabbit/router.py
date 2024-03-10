from typing import Any, Dict, Optional, Union

from typing_extensions import override

from faststream._compat import model_copy
from faststream.rabbit.asyncapi import Publisher
from faststream.rabbit.shared.router import RabbitRouter as BaseRouter
from faststream.rabbit.shared.schemas import (
    RabbitExchange,
    RabbitQueue,
)
from faststream.rabbit.shared.types import TimeoutType


class RabbitRouter(BaseRouter):
    """A class representing a RabbitMQ router for publishing messages.

    Attributes:
        _publishers : A dictionary mapping integer keys to Publisher objects

    Methods:
        _get_publisher_key : Returns the key for a given Publisher object
        _update_publisher_prefix : Updates the prefix of a given Publisher object
        publisher : Publishes a message to RabbitMQ

    """

    _publishers: Dict[int, Publisher]

    @staticmethod
    def _get_publisher_key(publisher: Publisher) -> int:
        """Get the publisher key.

        Args:
            publisher: The publisher object.

        Returns:
            The publisher key as an integer.

        """
        return publisher._get_routing_hash()

    @staticmethod
    def _update_publisher_prefix(prefix: str, publisher: Publisher) -> Publisher:
        """Updates the publisher prefix.

        Args:
            prefix (str): The prefix to be added to the publisher's queue name.
            publisher (Publisher): The publisher object to be updated.

        Returns:
            Publisher: The updated publisher object.

        Note:
            This function is intended to be used as a decorator.

        """
        publisher.queue = model_copy(
            publisher.queue, update={"name": prefix + publisher.queue.name}
        )
        return publisher

    @override
    def publisher(  # type: ignore[override]
        self,
        queue: Union[RabbitQueue, str] = "",
        exchange: Union[RabbitExchange, str, None] = None,
        *,
        routing_key: str = "",
        mandatory: bool = True,
        immediate: bool = False,
        timeout: TimeoutType = None,
        persist: bool = False,
        reply_to: Optional[str] = None,
        # AsyncAPI information
        title: Optional[str] = None,
        description: Optional[str] = None,
        schema: Optional[Any] = None,
        include_in_schema: bool = True,
        priority: Optional[int] = None,
        **message_kwargs: Any,
    ) -> Publisher:
        """Publishes a message to a RabbitMQ queue or exchange.

        Args:
            queue: The RabbitMQ queue to publish the message to. Can be either a RabbitQueue object or a string representing the queue name.
            exchange: The RabbitMQ exchange to publish the message to. Can be either a RabbitExchange object, a string representing the exchange name, or None.
            routing_key: The routing key to use when publishing the message.
            mandatory: Whether the message is mandatory or not.
            immediate: Whether the message should be delivered immediately or not.
            timeout: The timeout for the publish operation.
            persist: Whether the message should be persisted or not.
            reply_to: The reply-to address for the message.
            title: The title of the message (AsyncAPI information).
            description: The description of the message (AsyncAPI information).
            schema: The schema of the message (AsyncAPI information).
            include_in_schema: Whether to include the message in the API specification (AsyncAPI information).
            priority: The priority of the message.
            **message_kwargs: Additional keyword arguments to include in the message.

        Returns:
            The Publisher object used to publish the message.

        """
        new_publisher = self._update_publisher_prefix(
            self.prefix,
            Publisher(
                queue=RabbitQueue.validate(queue),
                exchange=RabbitExchange.validate(exchange),
                routing_key=routing_key,
                mandatory=mandatory,
                immediate=immediate,
                timeout=timeout,
                persist=persist,
                reply_to=reply_to,
                priority=priority,
                message_kwargs=message_kwargs,
                title=title,
                _description=description,
                _schema=schema,
                include_in_schema=(
                    include_in_schema
                    if self.include_in_schema is None
                    else self.include_in_schema
                ),
            ),
        )
        key = self._get_publisher_key(new_publisher)
        publisher = self._publishers[key] = self._publishers.get(key, new_publisher)
        return publisher
