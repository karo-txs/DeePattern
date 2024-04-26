from __future__ import annotations
from deepattern.objects.transitional_object import TransitionalObject
from deepattern.objects.logger_singleton import LoggerSingleton
from deepattern.objects.config_singleton import ConfigSingleton
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    depends_on: list = field(default_factory=list) 

    def verify_dependences(self, last_strategy: Strategy):
        return not self.depends_on or (self.depends_on and last_strategy.__class__ in [dep.__class__ for dep in self.depends_on])

    def load_conf_and_run_strategy(self, cfg: ConfigSingleton):
        self.cfg = cfg
        self.transitional_object = TransitionalObject() 
        self.logger = LoggerSingleton()
        
        self.logger.info(f"Strategy Started: {self.__str__()}")
        self.run_strategy()
        
    @abstractmethod
    def run_strategy(self) -> None:
        pass

    def __str__(self):
        return str(self.__class__.__name__)
    