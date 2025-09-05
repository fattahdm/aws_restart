import re

# Baca isi file
with open("preproinsulin-seq.txt", "r") as f:
    raw_seq = f.read()

# Bersihkan dengan regex:
# - hapus "ORIGIN" dan "//"
# - hapus angka
# - hapus spasi, newline, carriage return
clean_seq = re.sub(r'ORIGIN', '', raw_seq)
clean_seq = re.sub(r'//', '', clean_seq)
clean_seq = re.sub(r'\d+', '', clean_seq)
clean_seq = re.sub(r'\s+', '', clean_seq)

with open("clean_preproinsulin.txt", "w") as f:
    f.write(clean_seq)
    
print("Clean sequence:", clean_seq)
print("Length:", len(clean_seq))
