import argparse
from utils.data_loader import load_sentences
from evaluation.evaluator import Evaluator

def main(args):
    references = load_sentences(args.references)
    hypotheses = load_sentences(args.predictions)
    evaluator = Evaluator(references, hypotheses)
    results = evaluator.evaluate()
    for metric, score in results.items():
        print(f"{metric}: {score:.2f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", required=True, help="Fichier avec traductions générées")
    parser.add_argument("--references", required=True, help="Fichier avec traductions de référence")
    args = parser.parse_args()
    main(args)