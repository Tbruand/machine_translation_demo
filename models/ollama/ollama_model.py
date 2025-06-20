from models.base_model import BaseModel

class OllamaModel(BaseModel):
    def __init__(self, model_name: str):
        self.model_name = model_name
        # Initialisation modèle Ollama (à compléter)

    def translate(self, sentence: str, temperature: float = 0.5) -> str:
        # Implémenter appel modèle Ollama ici
        return f"Traduction Ollama ({self.model_name}): {sentence} (temp={temperature})"