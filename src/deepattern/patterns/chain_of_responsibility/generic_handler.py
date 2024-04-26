from deepattern.objects.config_singleton import ConfigSingleton
from deepattern.patterns import Handler
from dataclasses import dataclass
from abc import abstractmethod


@dataclass
class GenericHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    cfg: ConfigSingleton = None
    name: str = "none"
    _next_handler: Handler = None
    executed: bool = False

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self) -> None:
        if not self.executed:
            self.action()
            self.executed = True
            return self
        elif self._next_handler:
            return self._next_handler

        return None
    
    @abstractmethod
    def action(self) -> None:
        pass