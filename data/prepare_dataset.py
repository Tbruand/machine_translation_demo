from datasets import load_dataset
import os

def prepare_europarl_dataset():
    dataset = load_dataset("Nadas31/europarl-en-fr-translation")

    os.makedirs("data/processed", exist_ok=True)

    splits = dataset.keys()  # liste des splits disponibles

    print(f"Splits disponibles : {list(splits)}")

    for split in splits:
        src_file = f"data/processed/{split}_en.txt"
        tgt_file = f"data/processed/{split}_fr.txt"

        with open(src_file, "w", encoding="utf-8") as f_src, open(tgt_file, "w", encoding="utf-8") as f_tgt:
            for example in dataset[split]:
                f_src.write(example["translation"]["en"] + "\n")
                f_tgt.write(example["translation"]["fr"] + "\n")

    print("Dataset Europarl téléchargé et sauvegardé dans data/processed/")

if __name__ == "__main__":
    prepare_europarl_dataset()