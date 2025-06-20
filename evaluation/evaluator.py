from .metrics import compute_bleu, compute_rouge

class Evaluator:
    def __init__(self, references, hypotheses):
        self.references = references
        self.hypotheses = hypotheses

    def evaluate(self):
        bleu_score = compute_bleu(self.references, self.hypotheses)
        rouge_scores = compute_rouge(self.references, self.hypotheses)
        return {
            'BLEU': bleu_score,
            'ROUGE-1': rouge_scores['rouge1'],
            'ROUGE-L': rouge_scores['rougeL']
        }