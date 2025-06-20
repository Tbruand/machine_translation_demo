import random
import os

def split_train_val_test(src_file, tgt_file, output_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1, seed=42):
    random.seed(seed)

    os.makedirs(output_dir, exist_ok=True)

    with open(src_file, "r", encoding="utf-8") as f_src, open(tgt_file, "r", encoding="utf-8") as f_tgt:
        src_lines = f_src.readlines()
        tgt_lines = f_tgt.readlines()

    assert len(src_lines) == len(tgt_lines), "Source and target files must have the same number of lines"

    indices = list(range(len(src_lines)))
    random.shuffle(indices)

    n = len(indices)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)

    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train+n_val]
    test_idx = indices[n_train+n_val:]

    def write_split(name, idxs):
        with open(os.path.join(output_dir, f"{name}_en.txt"), "w", encoding="utf-8") as f_src_out, \
             open(os.path.join(output_dir, f"{name}_fr.txt"), "w", encoding="utf-8") as f_tgt_out:
            for i in idxs:
                f_src_out.write(src_lines[i])
                f_tgt_out.write(tgt_lines[i])

    write_split("train_80", train_idx)
    write_split("val_10", val_idx)
    write_split("test_10", test_idx)

    print(f"Split done: train_80 ({len(train_idx)}), val_10 ({len(val_idx)}), test_10 ({len(test_idx)})")

if __name__ == "__main__":
    split_train_val_test(
        "data/processed/train_en.txt",
        "data/processed/train_fr.txt",
        "data/processed"
    )