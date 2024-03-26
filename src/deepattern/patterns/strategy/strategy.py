from __future__ import annotations
from deepattern.objects import TransitionalObject
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    depends_on: List = []

    def verify_dependences(self, last_strategy: Strategy):
        return not self.depends_on or (self.depends_on and last_strategy.__class__ in [dep.__class__ for dep in self.depends_on])

    @abstractmethod
    def run_strategy(self, data: Optional[TransitionalObject]) -> Optional[TransitionalObject]:
        pass
    