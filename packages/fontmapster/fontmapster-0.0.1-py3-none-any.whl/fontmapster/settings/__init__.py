from dataclasses import dataclass, field
from importlib import import_module
from types import ModuleType
from typing import Any, Dict, Optional, Union

from fontmapster.settings import default_settings


@dataclass
class BaseSettings:
    _settings: dict = field(default_factory=dict)
    _frozen: bool = field(default=False, init=False)

    def get(self, key):
        return self._settings.get(key)

    def set(self, key, value):
        self._assert_mutability()
        self._settings[key] = value

    def set_module(self, module: Union[ModuleType, str]) -> None:
        if isinstance(module, str):
            module = import_module(module)
        for key in dir(module):
            if key.isupper():
                self.set(key, getattr(module, key))

    def update(self, values):
        self._assert_mutability()
        self._settings.update(values)

    def freeze(self):
        self._frozen = True

    def _assert_mutability(self) -> None:
        if self._frozen:
            raise TypeError("Trying to modify an immutable Settings object")


class Settings(BaseSettings):
    def __init__(self, values: Optional[dict] = None):
        super().__init__()
        self.set_module(default_settings)
        if not values:
            values = {}
        self.update(values)

    def asdict(self) -> Dict[str, Any]:
        return self._settings
