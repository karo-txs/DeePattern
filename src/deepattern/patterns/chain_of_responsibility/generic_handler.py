from deepattern.objects import TransitionalObject
from deepattern.patterns import Handler
from dataclasses import dataclass
from abc import abstractmethod
from typing import Optional


@dataclass
class GenericHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    name: str = "none"
    _next_handler: Handler = None
    executed: bool = True

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Optional[TransitionalObject]) -> Optional[TransitionalObject]:
        if not self.executed:
            self.action(request.data)
            self.executed = True
            return self
        elif self._next_handler:
            return self._next_handler

        return None
    
    @abstractmethod
    def action(self, data: Optional[TransitionalObject]) -> None:
        pass