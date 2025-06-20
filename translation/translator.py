from models.ollama.ollama_model import OllamaModel
from models.huggingface.hf_model import HuggingFaceModel

class Translator:
    def __init__(self):
        self.models = {
            'ollama_model_1': OllamaModel('ollama-model-1'),
            'huggingface_mbart': HuggingFaceModel('facebook/mbart-large-50-many-to-many-mmt'),
            # Ajouter d'autres modèles si besoin
        }

    def translate(self, sentence: str, model_name: str, temperature: float = 0.5):
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model '{model_name}' not found")
        return model.translate(sentence, temperature)