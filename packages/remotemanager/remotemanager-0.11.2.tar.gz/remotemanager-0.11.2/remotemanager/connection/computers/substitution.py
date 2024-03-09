import math
from typing import Union

from remotemanager.connection.computers.dynamicvalue import DynamicMixin


class Substitution(DynamicMixin):
    """
    Stores a jobscript template substitution

    Args:
        target:
            String to _replace_ in the template.
            Ideally should begin with a commenting character (#)
        entrypoint:
            String to replace _with_. At script generation, `target`
            will be replaced with `entrypoint`
    """

    __slots__ = ["target", "entrypoint", "mode", "executed", "dependencies"]

    def __init__(
        self,
        target: str,
        entrypoint: str,
        default=None,
        min: Union[int, None] = None,
        max: Union[int, None] = None,
        mode: Union[str, None] = None,
    ):
        super().__init__(assignment=entrypoint, default=default, min=min, max=max)

        self.target = target
        self.entrypoint = entrypoint
        self.mode = mode

        self.executed = False

        self.dependencies = []  # must calculate the value of these first

    def __hash__(self) -> int:
        return hash(self.target + self.entrypoint)

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return f"Substitution({self.target}, {self.entrypoint}) -> {self.value}"

    @property
    def value(self) -> any:
        """
        Returns:
            value if present, else default
        """
        val = super().value

        if len(self.dependencies) == 0:
            try:
                return math.ceil(val / 1)
            except TypeError:
                return val
        # if we have dependents, we need to evaluate them
        evaluate = {}
        # int values cause this replace to fail
        # non strings probably shouldn't end up here,
        # but it's best not to error weirdly
        val = str(val)
        for dep in self.dependencies:
            evaluate[dep.arg] = dep.value
            # replace the target $value with the evaluated arg
            # print(f"replacing {dep.arg} -> {dep.value}")
            val = val.replace(f"${dep.arg}", str(dep.value))
        # now everything is replaced, we can freely eval
        # print(f"evaluating {val}")
        val = eval(str(val.strip()))
        # print(f"{self.arg}={val}\n")
        # cache the result
        self.value = val
        self.dependencies = {}
        return val

    @value.setter
    def value(self, val):
        super().set_value(val)

    @property
    def arg(self) -> str:
        """
        Returns:
            Argument which is exposed to the underlying URL for setting
        """
        return self.entrypoint.strip("$")

    @property
    def name(self) -> str:
        """Returns the name/entrypoint for this sub"""
        return self.entrypoint

    @property
    def reduced(self):
        return self._value.reduced

    def pack(self) -> dict:
        """Store this Substitution in dict form"""
        data = {"target": self.target, "entrypoint": self.entrypoint}

        if self.mode is not None:
            data["mode"] = self.mode

        if getattr(self, "default", None) is not None:
            try:
                data["default"] = self.default.reduced
            except AttributeError:
                data["default"] = self.default

        return data
