import argparse
from translation.translator import Translator
from utils.data_loader import load_sentences

def main(args):
    translator = Translator()
    sentences = load_sentences(args.input)
    with open(args.output, "w", encoding="utf-8") as f_out:
        for sentence in sentences:
            translation = translator.translate(sentence, args.model, args.temp)
            f_out.write(translation + "\n")
    print(f"Traductions sauvegardées dans {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Nom du modèle à utiliser")
    parser.add_argument("--temp", type=float, default=0.5, help="Température de génération")
    parser.add_argument("--input", required=True, help="Fichier d'entrée avec phrases à traduire")
    parser.add_argument("--output", required=True, help="Fichier de sortie pour les traductions")
    args = parser.parse_args()
    main(args)