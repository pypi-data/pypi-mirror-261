from typing import Any, Callable, Sequence, Union

from aio_pika.message import IncomingMessage
from typing_extensions import override

from faststream._compat import model_copy
from faststream.broker.router import BrokerRoute as RabbitRoute
from faststream.broker.router import BrokerRouter
from faststream.broker.types import P_HandlerParams, T_HandlerReturn
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.rabbit.shared.schemas import RabbitQueue
from faststream.types import SendableMessage

__all__ = (
    "RabbitRoute",
    "RabbitRouter",
)


class RabbitRouter(BrokerRouter[int, IncomingMessage]):
    """A class representing a RabbitMQ router for handling incoming messages.

    Attributes:
        prefix : prefix for the queue name
        handlers : sequence of RabbitRoutes for handling incoming messages
        kwargs : additional keyword arguments

    Methods:
        __init__ : initializes the RabbitRouter object
        subscriber : decorator for subscribing to a queue and registering a handler function

    """

    def __init__(
        self,
        prefix: str = "",
        handlers: Sequence[RabbitRoute[IncomingMessage, SendableMessage]] = (),
        **kwargs: Any,
    ) -> None:
        """Override the `__init__` method of the parent class.

        Args:
            prefix: A prefix string
            handlers: A sequence of RabbitRoute objects
            **kwargs: Additional keyword arguments

        Raises:
            NotImplementedError: If silent animals are not supported

        """
        for h in handlers:
            if (q := h.kwargs.pop("queue", None)) is None:
                q, h.args = h.args[0], h.args[1:]
            queue = RabbitQueue.validate(q)
            new_q = model_copy(queue, update={"name": prefix + queue.name})
            h.args = (new_q, *h.args)

        super().__init__(prefix, handlers, **kwargs)

    @override
    def subscriber(  # type: ignore[override]
        self,
        queue: Union[str, RabbitQueue],
        *broker_args: Any,
        **broker_kwargs: Any,
    ) -> Callable[
        [Callable[P_HandlerParams, T_HandlerReturn]],
        HandlerCallWrapper[IncomingMessage, P_HandlerParams, T_HandlerReturn],
    ]:
        """A function to subscribe to a RabbitMQ queue.

        Args:
            self : the instance of the class
            queue : the queue to subscribe to, can be a string or a RabbitQueue object
            *broker_args : additional arguments for the broker
            **broker_kwargs : additional keyword arguments for the broker

        Returns:
            A callable object that wraps the handler function for the incoming messages from the queue.

        Raises:
            TypeError: If the queue is not a string or a RabbitQueue object

        """
        q = RabbitQueue.validate(queue)
        new_q = model_copy(q, update={"name": self.prefix + q.name})
        return self._wrap_subscriber(new_q, *broker_args, **broker_kwargs)
