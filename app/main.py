from typing import Any
from typing import Callable


def cache(func: Callable) -> None:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        wrapper_dict = {}

        if args in storage.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            wrapper_dict[args] = func(*args, **kwargs)
            storage.update(wrapper_dict)

        return storage[args]

    return wrapper
