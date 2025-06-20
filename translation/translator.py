from models.ollama.ollama_model import OllamaModel
from models.huggingface.hf_model import HuggingFaceModel

class Translator:
    def __init__(self):
        self.models = {
        'ollama_model_1': OllamaModel('ollama-model-1'),
        'huggingface_opus_mt_en_fr': HuggingFaceModel('Helsinki-NLP/opus-mt-en-fr'),
}

    def translate(self, sentence: str, model_name: str, temperature: float = 0.5, num_beams: int = 5):
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Model '{model_name}' not found")

        # Exemple de gestion simple pour HuggingFace (ignore temperature)
        if isinstance(model, HuggingFaceModel):
            return model.translate(sentence, temperature=temperature, num_beams=num_beams)
        else:
            return model.translate(sentence, temperature=temperature)