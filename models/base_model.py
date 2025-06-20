from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def translate(self, sentence: str, temperature: float = 0.5) -> str:
        pass