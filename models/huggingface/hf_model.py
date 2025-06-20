from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from models.base_model import BaseModel
from tqdm import tqdm
import time
import torch

class HuggingFaceModel(BaseModel):
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

    def translate_batch(self, sentences, batch_size=16, temperature: float = 0.5, num_beams: int = 5):
        translations = []
        for i in range(0, len(sentences), batch_size):
            batch = sentences[i:i+batch_size]
            inputs = self.tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=128)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            outputs = self.model.generate(**inputs, max_length=128, num_beams=num_beams)  # temperature ignorée ici
            decoded = [self.tokenizer.decode(t, skip_special_tokens=True) for t in outputs]
            translations.extend(decoded)
        return translations

    def translate(self, sentence: str, temperature: float = 0.5, num_beams: int = 5) -> str:
        return self.translate_batch([sentence], temperature=temperature, num_beams=num_beams)[0]