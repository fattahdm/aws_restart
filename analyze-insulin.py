import re

# Baca file sumber
with open("preproinsulin-seq.txt", "r") as f:
    raw_seq = f.read()

# Bersihkan dengan regex
clean_seq = re.sub(r'ORIGIN', '', raw_seq)
clean_seq = re.sub(r'//', '', clean_seq)
clean_seq = re.sub(r'\d+', '', clean_seq)
clean_seq = re.sub(r'\s+', '', clean_seq)

# Simpan full clean sequence
with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(clean_seq)

# Potongan
ls = clean_seq[0:24]     # 1–24
bs = clean_seq[24:54]    # 25–54
cs = clean_seq[54:89]    # 55–89
as_ = clean_seq[89:110]  # 90–110

# Simpan masing-masing
with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(ls)

with open("binsulin-seq-clean.txt", "w") as f:
    f.write(bs)

with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(cs)

with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(as_)

# Print untuk verifikasi
print("Full sequence length:", len(clean_seq))
print("L-seq (1–24):", len(ls), ls)
print("B-seq (25–54):", len(bs), bs)
print("C-seq (55–89):", len(cs), cs)
print("A-seq (90–110):", len(as_), as_)