import inspect
import json
from contextlib import suppress
from functools import partial
from typing import Any, Optional, Sequence, Tuple, Union, cast, overload

from faststream._compat import dump_json, json_loads
from faststream.broker.message import StreamMessage
from faststream.broker.types import (
    AsyncCustomDecoder,
    AsyncCustomParser,
    AsyncDecoder,
    AsyncParser,
    CustomDecoder,
    CustomParser,
    Decoder,
    MsgType,
    Parser,
    StreamMsg,
    SyncDecoder,
    SyncParser,
)
from faststream.constants import ContentType, ContentTypes
from faststream.types import DecodedMessage, SendableMessage


def decode_message(message: StreamMessage[Any]) -> DecodedMessage:
    """Decodes a message.

    Args:
        message: The message to decode.

    Returns:
        The decoded message.

    Raises:
        JSONDecodeError: If the message body cannot be decoded as JSON.

    """
    body: Any = getattr(message, "body", message)
    m: DecodedMessage = body

    if content_type := getattr(message, "content_type", None):
        if ContentTypes.text.value in content_type:
            m = body.decode()
        elif ContentTypes.json.value in content_type:  # pragma: no branch
            m = json_loads(body)

    else:
        with suppress(json.JSONDecodeError):
            m = json_loads(body)

    return m


def encode_message(
    msg: Union[Sequence[SendableMessage], SendableMessage],
) -> Tuple[bytes, Optional[ContentType]]:
    """Encodes a message.

    Args:
        msg: The message to be encoded.

    Returns:
        A tuple containing the encoded message as bytes and the content type of the message.

    """
    if msg is None:
        return b"", None

    if isinstance(msg, bytes):
        return msg, None

    if isinstance(msg, str):
        return msg.encode(), ContentTypes.text.value

    return (
        dump_json(msg),
        ContentTypes.json.value,
    )


@overload
def resolve_custom_func(
    custom_func: Optional[SyncDecoder[StreamMsg]],
    default_func: SyncDecoder[StreamMsg],
) -> SyncDecoder[StreamMsg]:
    """Resolve a custom function.

    Args:
        custom_func: A custom function of type SyncDecoder
        default_func: A default function of type SyncDecoder

    Returns:
        A resolved function of type SyncDecoder

    """
    ...


@overload
def resolve_custom_func(
    custom_func: Optional[SyncParser[MsgType, StreamMsg]],
    default_func: SyncParser[MsgType, StreamMsg],
) -> SyncParser[MsgType, StreamMsg]:
    """Resolve a custom function.

    Args:
        custom_func: A custom function of type SyncParser[MsgType]. Optional.
        default_func: A default function of type SyncParser[MsgType].

    Returns:
        A resolved function of type SyncParser[MsgType].

    """
    ...


@overload
def resolve_custom_func(
    custom_func: Optional[AsyncCustomDecoder[StreamMsg]],
    default_func: AsyncDecoder[StreamMsg],
) -> AsyncDecoder[StreamMsg]:
    """Resolve a custom function.

    Args:
        custom_func: Optional custom function to be resolved.
        default_func: Default function to be used if custom function is not provided.

    Returns:
        Resolved function.

    """
    ...


@overload
def resolve_custom_func(
    custom_func: Optional[AsyncCustomParser[MsgType, StreamMsg]],
    default_func: AsyncParser[MsgType, StreamMsg],
) -> AsyncParser[MsgType, StreamMsg]:
    """Resolve a custom function.

    Args:
        custom_func: Optional custom function to be resolved.
        default_func: Default function to be used if custom function is not provided.

    Returns:
        Resolved function.

    """
    ...


@overload
def resolve_custom_func(
    custom_func: Optional[CustomDecoder[StreamMsg]],
    default_func: Decoder[StreamMsg],
) -> Decoder[StreamMsg]:
    """Resolve a custom function.

    Args:
        custom_func: A custom decoder function.
        default_func: A default decoder function.

    Returns:
        A decoder function.

    """
    ...


@overload
def resolve_custom_func(
    custom_func: Optional[CustomParser[MsgType, StreamMsg]],
    default_func: Parser[MsgType, StreamMsg],
) -> Parser[MsgType, StreamMsg]:
    """Resolve a custom function.

    Args:
        custom_func: Optional custom function to be resolved.
        default_func: Default function to be used if custom function is not provided.

    Returns:
        Resolved function.

    """
    ...


def resolve_custom_func(  # type: ignore[misc]
    custom_func: Optional[
        Union[CustomDecoder[StreamMsg], CustomParser[MsgType, StreamMsg]]
    ],
    default_func: Union[Decoder[StreamMsg], Parser[MsgType, StreamMsg]],
) -> Union[Decoder[StreamMsg], Parser[MsgType, StreamMsg]]:
    """Resolve a custom function.

    Args:
        custom_func: Optional custom function of type CustomDecoder or CustomParser.
        default_func: Default function of type Decoder or Parser.

    Returns:
        The resolved function of type Decoder or Parser.

    """
    if custom_func is None:
        return default_func

    original_params = inspect.signature(custom_func).parameters
    if len(original_params) == 1:
        return cast(Union[Decoder[StreamMsg], Parser[MsgType, StreamMsg]], custom_func)

    else:
        name = tuple(original_params.items())[1][0]
        return partial(custom_func, **{name: default_func})  # type: ignore
