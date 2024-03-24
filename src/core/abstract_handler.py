from core import TransitionalObject, Handler, RequestObject, Strategy
from __future__ import annotations
from dataclasses import dataclass
from abc import abstractmethod
from typing import Optional

@dataclass
class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    name: str = "none"
    strategy: Strategy
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Optional[RequestObject]) -> Optional[TransitionalObject]:
        if self.name == request.name:
            return self.action(request.data)
        elif self._next_handler:
            return self._next_handler.handle(request)

        return None
    
    @abstractmethod
    def action(self, data: Optional[TransitionalObject]) -> Optional[TransitionalObject]:
        return self.strategy.run_strategy(data)