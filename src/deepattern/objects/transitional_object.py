from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TransitionalObject(object):
    name: str = "none"
    data: any = None

    def create_attr(self, attr_name, value) -> TransitionalObject:
        setattr(self, attr_name, value)
        return self