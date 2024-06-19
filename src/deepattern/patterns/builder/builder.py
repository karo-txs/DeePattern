from __future__ import annotations
from deepattern.objects.config_singleton import ConfigSingleton
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ModelBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Model objects.
    """

    cfg: ConfigSingleton = None

    @property
    @abstractmethod
    def model(self) -> None:
        pass

    @abstractmethod
    def include_input(self) -> None:
        pass

    @abstractmethod
    def include_hidden(self) -> None:
        pass

    @abstractmethod
    def include_output(self) -> None:
        pass

    @abstractmethod
    def compile(self) -> None:
        pass
