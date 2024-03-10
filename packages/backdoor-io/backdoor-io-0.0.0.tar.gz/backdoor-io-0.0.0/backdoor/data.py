# data.py

import json
import time
from typing import Literal, Self
from dataclasses import dataclass, field, asdict

from dacite import from_dict

__all__ = [
    "Format",
    "Data"
]

Formatter = Literal['text', 'json', 'binary']
JsonValue = str | bytes | dict | list | int | float | bool | None

class Format:

    TEXT = 'text'
    BYTES = 'bytes'
    JSON = 'json'

    @staticmethod
    def encode(data: JsonValue) -> str:

        if not isinstance(data, (str, bytes)):
            data = json.dumps(data)

        if isinstance(data, str):
            return data

        if isinstance(data, bytes):
            return data.decode()

        raise TypeError(f"invalid data type: {type(data)}")

    @staticmethod
    def decode(data: str, f: str | Formatter) -> JsonValue:

        if f == 'binary':
            return data.encode()

        if f == 'text':
            return data

        if f == 'json':
            return json.loads(data)

        raise TypeError(f"invalid format: {f}")

    @staticmethod
    def format(data: JsonValue) -> str:

        if isinstance(data, bytes):
            return Format.BYTES

        elif isinstance(data, str):
            return Format.TEXT

        elif isinstance(data, (int, float, type(None), dict, list, tuple)):
            return Format.JSON

        raise TypeError(f"invalid data type: {type(data)}")

@dataclass(slots=True)
class Data:

    payload: JsonValue = None
    format: str | Formatter | None = None
    name: str | None = None
    read: bool | None = None
    write: bool | None = None
    timestamp: int = field(default_factory=time.time)

    def __post_init__(self) -> None:

        if self.read or self.write:
            self.read = not self.write
            self.write = not self.read

        else:
            self.read = False
            self.write = False

        self.data()

    @property
    def io(self) -> bool:

        return self.read or self.write

    @property
    def valid(self) -> bool:

        return not (self.io and (not self.name))

    def data(self) -> JsonValue:

        if (self.format is None) and (self.payload is not None):
            self.format = Format.format(self.payload)

        elif (self.format is not None) and (self.format != Format.format(self.payload)):
            # noinspection PyTypeChecker
            self.payload = Format.decode(self.payload, self.format)

        return self.payload

    def upload(self, memory: dict[str, ...]) -> bool:

        if self.name and self.read:
            self.payload = memory[self.name]

            return True

        return False

    def update(self, memory: dict[str, ...], value: ... = Ellipsis) -> bool:

        if value == Ellipsis:
            value = self.data()

        flag = self.name and self.write

        if flag:
            memory[self.name] = value

        return flag

    @classmethod
    def load(cls, data: dict[str, JsonValue]) -> Self:

        data = data.copy()

        if None not in (data['payload'], data['format']):
            data['payload'] = Format.decode(data['payload'], data['format'])

        return from_dict(cls, data)

    def dump(self) -> dict[str, JsonValue]:

        data = asdict(self)
        data['payload'] = Format.encode(data['payload'])

        return data

    def copy(self) -> Self:

        data = self.dump()
        data.pop('timestamp')

        new = type(self).load(data)

        return new
