import time
from functools import wraps
from typing import Any, Callable


def throttle(seconds: float) -> Callable[..., Any]:
    """Throttle a function to ensure it is called no more than every n seconds.

    Args:
       seconds (float): Throttle time.

    Returns:
       Callable: Throttled function.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        last_called: float = 0
        last_result: Any = None

        @wraps(func)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_called
            nonlocal last_result
            current_time = time.time()
            if current_time - last_called >= seconds:
                last_result = func(*args, **kwargs)
                last_called = current_time
            return last_result

        return wrapped

    return decorator
