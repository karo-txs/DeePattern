from deepattern.patterns import GenericHandler, Handler, Context
from deepattern.objects import TransitionalObject
from dataclasses import dataclass
from typing import Optional


@dataclass
class StrategyHandler(GenericHandler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    name: str = "none"
    context: Context = None
    _next_handler: Handler = None
    executed: bool = False

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: Optional[TransitionalObject] = None) -> Optional[TransitionalObject]:
        if not self.executed:
            self.action(request)
            self.executed = True
            return self
        elif self._next_handler:
            return self._next_handler.handle(request)

        return None
    
    def action(self, data: Optional[TransitionalObject] = None) -> None:
        self.context.run_strategy(data)