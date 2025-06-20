import os

def sample_50():
    os.makedirs("data/processed", exist_ok=True)
    src_in = "data/processed/train_en.txt"
    tgt_in = "data/processed/train_fr.txt"
    src_out = "data/processed/test_50_en.txt"
    tgt_out = "data/processed/test_50_fr.txt"

    with open(src_in, "r", encoding="utf-8") as f_src, open(tgt_in, "r", encoding="utf-8") as f_tgt:
        src_lines = f_src.readlines()
        tgt_lines = f_tgt.readlines()

    assert len(src_lines) == len(tgt_lines), "Mismatch source/target line count"

    n = min(50, len(src_lines))
    with open(src_out, "w", encoding="utf-8") as f_src_out, open(tgt_out, "w", encoding="utf-8") as f_tgt_out:
        for i in range(n):
            f_src_out.write(src_lines[i])
            f_tgt_out.write(tgt_lines[i])

    print(f"Sampled {n} lines to {src_out} and {tgt_out}")

if __name__ == "__main__":
    sample_50()