from __future__ import annotations
from deepattern.patterns import GenericHandler, Handler, Context, Strategy
from deepattern.objects import TransitionalObject
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class StrategyHandler(GenericHandler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    context: Context = None
    request: TransitionalObject = TransitionalObject()
    chain_execution: List = field(default_factory=[])
    
    @classmethod
    def builder(cls, strategy: Strategy) -> StrategyHandler:
        return StrategyHandler(context=Context(strategy=strategy))
    
    @classmethod
    def builder(cls, strategies: List[Strategy]) -> StrategyHandler:
        handler = StrategyHandler(context=Context(strategy=strategies[0]))
        for strategy in strategies[1:]:
            handler = handler.set_next(StrategyHandler(context=Context(strategy=strategy)))
        return handler

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self) -> StrategyHandler:
        self.chain_execution.append(self.context.strategy)
        
        if not self.context.strategy.verify_dependences(self.chain_execution[-1]):
            raise "Chain Broken. Verify Strategy Dependences"

        if not self.executed:
            self.request = self.action(self.request)
            self.executed = True
            return self
        elif self._next_handler:
            return self._next_handler.handle(self.request)

        return None
    
    def action(self, data: Optional[TransitionalObject] = None) -> Optional[TransitionalObject]:
        return self.context.run_strategy(data)