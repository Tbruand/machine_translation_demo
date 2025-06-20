from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from models.base_model import BaseModel

class HuggingFaceModel(BaseModel):
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate(self, sentence: str, temperature: float = 0.5) -> str:
        inputs = self.tokenizer(sentence, return_tensors="pt")
        outputs = self.model.generate(**inputs, temperature=temperature, max_length=128)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)