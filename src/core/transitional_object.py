from dataclasses import dataclass


@dataclass
class TransitionalObject(object):
    name: str = "none"
    data: any = None