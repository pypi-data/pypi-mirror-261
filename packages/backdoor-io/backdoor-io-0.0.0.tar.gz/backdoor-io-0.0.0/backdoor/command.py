# command.py

import json
from uuid import uuid4
from typing import Self, Callable
from dataclasses import dataclass, field, asdict

from dacite import from_dict

from backdoor.action import Action
from backdoor.data import Data, Format
from backdoor.execution import SubProcess, SubThread

__all__ = [
    "Command",
    "CommandCapsule",
    "save_command_json",
    "load_command_json"
]

JsonValue = str | bytes | dict | list | int | float | bool | None

@dataclass(slots=True)
class Command:

    action: Action | None = None
    id: str = field(default_factory=lambda: str(uuid4()))
    request: Data = field(default_factory=Data)
    response: Data = field(default_factory=Data)
    memory: dict[str, JsonValue] = field(default=None)
    complete: bool = False
    running: bool = False
    error: str | None = None
    executions: list[SubProcess | SubThread] = field(
        init=False, default_factory=list, repr=False
    )

    def __post_init__(self) -> None:

        from backdoor.actions import Actions

        if (
            (self.action is not None) and
            (self.action.type == Actions.DATA.TYPE)
        ):
            if (
                (self.request.write is None) and
                (self.action.name == Actions.DATA.WRITE)
            ):
                self.request.write = True
                self.request.read = False

            elif (
                (self.request.read is None) and
                (self.action.name == Actions.DATA.READ)
            ):
                self.request.write = False
                self.request.read = True

        elif self.action is None:
            if self.request.write:
                self.request.write = True
                self.request.read = False

                self.action = Action(
                    type=Actions.DATA.TYPE,
                    name=Actions.DATA.WRITE
                )

            elif self.request.read:
                self.request.write = False
                self.request.read = True

                self.action = Action(
                    type=Actions.DATA.TYPE,
                    name=Actions.DATA.READ
                )

    @property
    def io(self) -> bool:

        return self.response.io or self.request.io

    @property
    def valid(self) -> bool:

        return self.request.valid and self.response.valid

    def stop(self) -> None:

        for execution in self.executions:
            execution.terminate()

        self.executions.clear()

        self.running = False

    def respond(self, value: JsonValue, name: str = None) -> Data:

        self.response = self.response.copy()

        self.response.payload = value
        self.response.name = name
        self.response.format = Format.format(value)

        return self.response

    @classmethod
    def load(cls, data: dict[str, JsonValue | dict[str, JsonValue]]) -> Self:

        return from_dict(cls, data)

    def dump(self) -> dict[str, JsonValue | dict[str, JsonValue]]:

        data = asdict(self.copy())
        data.pop('executions')

        return data

    def copy(self) -> Self:

        return Command(
            id=self.id,
            action=self.action,
            request=self.request,
            response=self.response,
            complete=self.complete,
            running=self.running,
            error=self.error
        )

@dataclass(slots=True, frozen=True)
class CommandCapsule:

    command: Command
    memory: dict[str, ...] = field(default_factory=dict)
    on_finish: Callable[["CommandCapsule"], ...] = None

def save_command_json(command: Command, location: str = None) -> None:

    if location is None:
        location = ""

    else:
        location += "/"

    with open(f"{location}{command.id}.json", 'w') as file:
        json.dump(command.dump(), file, indent=4)

def load_command_json(path: str) -> Command:

    with open(path, 'r') as file:
        return Command.load(json.load(file))
