from deepattern.objects import TransitionalObject
from abc import ABC, abstractmethod
from typing import Optional


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def run_strategy(self, data: Optional[TransitionalObject]) -> Optional[TransitionalObject]:
        pass