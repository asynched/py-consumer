from functools import wraps
from threading import Thread
from typing import Callable


def thread(fn: Callable[[], None]):
    @wraps(fn)
    def decorated():
        thread = Thread(target=fn)
        thread.start()
        return thread

    return decorated
