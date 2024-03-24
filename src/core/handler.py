from core import TransitionalObject, RequestObject
from abc import ABC, abstractmethod
from __future__ import annotations
from typing import Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: Optional[RequestObject]) -> Optional[TransitionalObject]:
        pass
