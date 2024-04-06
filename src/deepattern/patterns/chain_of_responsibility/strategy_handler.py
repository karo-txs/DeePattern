from __future__ import annotations
from deepattern.patterns import GenericHandler, Handler, Context, Strategy
from dataclasses import dataclass, field
from typing import List


@dataclass
class StrategyHandler(GenericHandler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    context: Context = None
    chain_execution: list = field(default_factory=list) 
    
    @classmethod
    def builder(cls, strategy: Strategy) -> StrategyHandler:
        return StrategyHandler(context=Context(strategy=strategy))
    
    @classmethod
    def builder(cls, strategies: List[Strategy]) -> StrategyHandler:
        first_handler = StrategyHandler(context=Context(strategy=strategies[0]))
        next_handler = None
        is_first = True
        for strategy in strategies[1:]:
            if is_first:
                is_first = not is_first
                next_handler = StrategyHandler(context=Context(strategy=strategy))
                handler = first_handler.set_next(next_handler)
            else:
                next_handler = StrategyHandler(context=Context(strategy=strategy))
                handler = handler.set_next(next_handler)
        return first_handler

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self) -> StrategyHandler:
        self.chain_execution.append(self.context.strategy)
        
        if not self.context.strategy.verify_dependences(self.chain_execution[-1]):
            raise "Chain Broken. Verify Strategy Dependences"

        if not self.executed:
            self.action()
            self.executed = True
            return self
        
        elif self._next_handler:
            return self._next_handler.handle()

        return None
    
    def action(self) -> None:
        self.context.run_strategy()