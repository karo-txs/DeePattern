from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class ModelBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Model objects.
    """

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
