from abc import ABC, abstractmethod

class BaseTool(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_declaration(self):
        pass
