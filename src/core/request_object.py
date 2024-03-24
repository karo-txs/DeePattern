from core import TransitionalObject
from dataclasses import dataclass


@dataclass
class RequestObject(object):
    type: str = "none"
    data: TransitionalObject = None