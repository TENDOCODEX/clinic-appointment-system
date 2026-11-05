from abc import ABC, abstractmethod


class Lecturer(ABC):

    def __init__(self, module_name):
        if not isinstance(module_name, str) or not module_name.strip():
            raise ValueError("Module name cannot be empty")

        self._module_name = module_name.strip()

    @property
    def module_name(self):
        return self._module_name

    @abstractmethod
    def role(self):
        pass