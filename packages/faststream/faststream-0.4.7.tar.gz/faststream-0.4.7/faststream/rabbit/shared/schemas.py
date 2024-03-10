import warnings
from dataclasses import dataclass, field
from typing import Optional, Pattern

from pydantic import BaseModel

from faststream._compat import PYDANTIC_V2
from faststream.broker.schemas import NameRequired
from faststream.rabbit.shared.constants import ExchangeType
from faststream.rabbit.shared.types import TimeoutType
from faststream.types import AnyDict
from faststream.utils.path import compile_path


class RabbitQueue(NameRequired):
    """A class to represent a RabbitMQ queue.

    Attributes:
        name : name of the queue
        durable : whether the queue is durable or not
        exclusive : whether the queue is exclusive or not
        passive : whether the queue is passive or not
        auto_delete : whether the queue is auto delete or not
        arguments : additional arguments for the queue
        timeout : timeout for the queue
        robust : whether the queue is robust or not
        routing_key : routing key for the queue
        bind_arguments : additional arguments for binding the queue

    Methods:
        __hash__ : returns the hash value of the queue
        routing : returns the routing key of the queue
        __init__ : initializes the RabbitQueue object with the given parameters

    """

    name: str = ""
    durable: bool = False
    exclusive: bool = False
    passive: bool = False
    auto_delete: bool = False
    arguments: Optional[AnyDict] = None
    timeout: TimeoutType = None
    robust: bool = True

    routing_key: str = ""
    path_regex: Optional[Pattern[str]] = None
    bind_arguments: Optional[AnyDict] = None

    def __hash__(self) -> int:
        return sum(
            (
                hash(self.name),
                int(self.durable),
                int(self.exclusive),
                int(self.auto_delete),
            )
        )

    @property
    def routing(self) -> str:
        return self.routing_key or self.name

    def __init__(
        self,
        name: str,
        durable: bool = False,
        exclusive: bool = False,
        passive: bool = False,
        auto_delete: bool = False,
        arguments: Optional[AnyDict] = None,
        timeout: TimeoutType = None,
        robust: bool = True,
        bind_arguments: Optional[AnyDict] = None,
        routing_key: str = "",
    ) -> None:
        """Initialize a class object.

        Args:
            name (str): The name of the object.
            durable (bool, optional): Whether the object is durable. Defaults to False.
            exclusive (bool, optional): Whether the object is exclusive. Defaults to False.
            passive (bool, optional): Whether the object is passive. Defaults to False.
            auto_delete (bool, optional): Whether the object is auto delete. Defaults to False.
            arguments (dict, optional): Additional arguments for the object. Defaults to None.
            timeout (TimeoutType, optional): Timeout for the object. Defaults to None.
            robust (bool, optional): Whether the object is robust. Defaults to True.
            bind_arguments (dict, optional): Bind arguments for the object. Defaults to None.
            routing_key (str, optional): Routing key for the object. Defaults to "".

        """
        re, routing_key = compile_path(
            routing_key,
            replace_symbol="*",
            patch_regex=lambda x: x.replace(r"\#", ".+"),
        )

        super().__init__(
            name=name,
            path_regex=re,
            durable=durable,
            exclusive=exclusive,
            bind_arguments=bind_arguments,
            routing_key=routing_key,
            robust=robust,
            passive=passive,
            auto_delete=auto_delete,
            arguments=arguments,
            timeout=timeout,
        )

    if PYDANTIC_V2:
        model_config = {"arbitrary_types_allowed": True}
    else:

        class Config:
            arbitrary_types_allowed = True


class RabbitExchange(NameRequired):
    """A class to represent a RabbitMQ exchange.

    Attributes:
        name : name of the exchange
        type : type of the exchange
        durable : whether the exchange is durable or not
        auto_delete : whether the exchange is auto-deleted or not
        internal : whether the exchange is internal or not
        passive : whether the exchange is passive or not
        arguments : additional arguments for the exchange
        timeout : timeout for the exchange
        robust : whether the exchange is robust or not
        bind_to : exchange to bind to
        bind_arguments : additional arguments for the binding
        routing_key : routing key for the exchange

    Methods:
        __hash__ : returns the hash value of the exchange
        __init__ : initializes the RabbitExchange object

    """

    type: str = ExchangeType.DIRECT.value
    durable: bool = False
    auto_delete: bool = False
    internal: bool = False
    passive: bool = False
    arguments: Optional[AnyDict] = None
    timeout: TimeoutType = None
    robust: bool = True

    bind_to: Optional["RabbitExchange"] = None
    bind_arguments: Optional[AnyDict] = None
    routing_key: str = ""

    def __hash__(self) -> int:
        return sum(
            (
                hash(self.name),
                hash(self.type),
                hash(self.routing_key),
                int(self.durable),
                int(self.auto_delete),
            )
        )

    def __init__(
        self,
        name: str,
        type: ExchangeType = ExchangeType.DIRECT,
        durable: bool = False,
        auto_delete: bool = False,
        internal: bool = False,
        passive: bool = False,
        arguments: Optional[AnyDict] = None,
        timeout: TimeoutType = None,
        robust: bool = True,
        bind_to: Optional["RabbitExchange"] = None,
        bind_arguments: Optional[AnyDict] = None,
        routing_key: str = "",
    ) -> None:
        """Initialize a RabbitExchange object.

        Args:
            name (str): Name of the exchange.
            type (ExchangeType, optional): Type of the exchange. Defaults to ExchangeType.DIRECT.
            durable (bool, optional): Whether the exchange should survive broker restarts. Defaults to False.
            auto_delete (bool, optional): Whether the exchange should be deleted when no longer in use. Defaults to False.
            internal (bool, optional): Whether the exchange is used for internal purposes and should not be published to directly. Defaults to False.
            passive (bool, optional): Whether to check if the exchange exists before creating it. Defaults to False.
            arguments (Optional[AnyDict], optional): Additional arguments for the exchange. Defaults to None.
            timeout (TimeoutType, optional): Timeout for the operation. Defaults to None.
            robust (bool, optional): Whether to use robust mode for the exchange. Defaults to True.
            bind_to (Optional["RabbitExchange"], optional): Exchange to bind to. Defaults to None.
            bind_arguments (Optional[AnyDict], optional): Arguments for the binding. Defaults to None.
            routing_key (str, optional): Routing key for the exchange. Defaults to "".

        Raises:
            NotImplementedError:

        """
        if routing_key and bind_to is None:  # pragma: no cover
            warnings.warn(
                (
                    "\nRabbitExchange `routing_key` is using to bind exchange to another one"
                    "\nIt can be used only with the `bind_to` argument, please setup it too"
                ),
                category=RuntimeWarning,
                stacklevel=1,
            )

        super().__init__(
            name=name,
            type=type.value,
            durable=durable,
            auto_delete=auto_delete,
            routing_key=routing_key,
            bind_to=bind_to,
            bind_arguments=bind_arguments,
            robust=robust,
            internal=internal,
            passive=passive,
            timeout=timeout,
            arguments=arguments,
        )


class ReplyConfig(BaseModel):
    """A class to represent a reply configuration."""

    mandatory: bool = True
    immediate: bool = False
    persist: bool = False


def get_routing_hash(
    queue: RabbitQueue,
    exchange: Optional[RabbitExchange] = None,
) -> int:
    """Calculate the routing hash for a RabbitMQ queue and exchange.

    Args:
        queue: The RabbitMQ queue.
        exchange: The RabbitMQ exchange (optional).

    Returns:
        The routing hash as an integer.

    """
    return hash(queue) + hash(exchange or "")


@dataclass
class BaseRMQInformation:
    """BaseRMQInformation.

    Attributes:
        queue : RabbitQueue object representing the queue
        exchange : Optional RabbitExchange object representing the exchange
        _description : Optional string describing the class

    """

    queue: RabbitQueue = field(default=RabbitQueue(""))
    exchange: Optional[RabbitExchange] = field(default=None)
    _description: Optional[str] = field(default=None)
    virtual_host: str = "/"
