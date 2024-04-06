from __future__ import annotations
from deepattern.patterns.singleton.singleton_meta import SingletonMeta
from dataclasses import dataclass


@dataclass
class TransitionalObject(metaclass=SingletonMeta):
    name: str = "none"
    data: any = None

    def create_attr(self, attr_name, value) -> TransitionalObject:
        setattr(self, attr_name, value)
        return self