import sacrebleu
from rouge_score import rouge_scorer

def compute_bleu(reference_list, hypothesis_list):
    bleu = sacrebleu.corpus_bleu(hypothesis_list, [reference_list])
    return bleu.score

def compute_rouge(reference_list, hypothesis_list):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = [scorer.score(ref, hyp) for ref, hyp in zip(reference_list, hypothesis_list)]
    avg_rouge1 = sum(score['rouge1'].fmeasure for score in scores) / len(scores)
    avg_rougeL = sum(score['rougeL'].fmeasure for score in scores) / len(scores)
    return {'rouge1': avg_rouge1 * 100, 'rougeL': avg_rougeL * 100}