import inspect
from contextlib import asynccontextmanager
from functools import wraps
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    ContextManager,
    List,
    Optional,
    Union,
    overload,
)

import anyio
from fast_depends.core import CallModel
from fast_depends.utils import run_async as call_or_await

from faststream.types import AnyCallable, F_Return, F_Spec

__all__ = (
    "call_or_await",
    "get_function_positional_arguments",
    "to_async",
)


@overload
def to_async(
    func: Callable[F_Spec, Awaitable[F_Return]],
) -> Callable[F_Spec, Awaitable[F_Return]]:
    """Convert a synchronous function to an asynchronous function.

    Args:
        func: The synchronous function to be converted.

    Returns:
        The converted asynchronous function.

    Note:
        This function is used as a decorator to convert a synchronous function to an asynchronous function.
    """
    ...


@overload
def to_async(func: Callable[F_Spec, F_Return]) -> Callable[F_Spec, Awaitable[F_Return]]:
    """Convert a synchronous function to an asynchronous function.

    Args:
        func: The synchronous function to be converted.

    Returns:
        The asynchronous version of the function.
    """
    ...


def to_async(
    func: Union[
        Callable[F_Spec, F_Return],
        Callable[F_Spec, Awaitable[F_Return]],
    ],
) -> Callable[F_Spec, Awaitable[F_Return]]:
    """Converts a synchronous function to an asynchronous function.

    Args:
        func: The synchronous function to be converted.

    Returns:
        The asynchronous version of the input function.
    """

    @wraps(func)
    async def to_async_wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:
        """Wraps a function to make it asynchronous.

        Args:
            func: The function to be wrapped
            args: Positional arguments to be passed to the function
            kwargs: Keyword arguments to be passed to the function

        Returns:
            The result of the wrapped function

        Raises:
            Any exceptions raised by the wrapped function
        """
        return await call_or_await(func, *args, **kwargs)

    return to_async_wrapper


def get_function_positional_arguments(func: AnyCallable) -> List[str]:
    """Get the positional arguments of a function.

    Args:
        func: The function to get the positional arguments from.

    Returns:
        A list of strings representing the names of the positional arguments.
    """
    signature = inspect.signature(func)

    arg_kinds = (
        inspect.Parameter.POSITIONAL_ONLY,
        inspect.Parameter.POSITIONAL_OR_KEYWORD,
    )

    return [
        param.name for param in signature.parameters.values() if param.kind in arg_kinds
    ]


def timeout_scope(
    timeout: Optional[float] = 30,
    raise_timeout: bool = False,
) -> ContextManager[anyio.CancelScope]:
    scope: Callable[[Optional[float]], ContextManager[anyio.CancelScope]]
    scope = anyio.fail_after if raise_timeout else anyio.move_on_after  # type: ignore[assignment]

    return scope(timeout)


@asynccontextmanager
async def fake_context(*args: Any, **kwargs: Any) -> AsyncIterator[None]:
    yield None


def drop_response_type(
    model: CallModel[F_Spec, F_Return],
) -> CallModel[F_Spec, F_Return]:
    model.response_model = None
    return model
