import os
from translation.translator import Translator
from utils.data_loader import load_sentences
from tqdm import tqdm

def main(args):
    translator = Translator()
    sentences = load_sentences(args.input)
    
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    if hasattr(translator.models[args.model], "translate_batch"):
        translations = translator.models[args.model].translate_batch(
            sentences, temperature=args.temp, num_beams=args.num_beams
        )
        with open(args.output, "w", encoding="utf-8") as f_out:
            for t in translations:
                f_out.write(t + "\n")
        print(f"Traductions sauvegardées dans {args.output}")
    else:
        # fallback phrase par phrase avec tqdm
        with open(args.output, "w", encoding="utf-8") as f_out:
            for sentence in tqdm(sentences, desc="Traduction en cours"):
                translation = translator.translate(sentence, args.model, temperature=args.temp, num_beams=args.num_beams)
                f_out.write(translation + "\n")
        print(f"Traductions sauvegardées dans {args.output}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--temp", type=float, default=0.5)
    parser.add_argument("--num_beams", type=int, default=5)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args)