# Solution
```py
import ctypes

libc = ctypes.CDLL("/usr/lib/libc.so.6")

seed = 0xde

with open("flag.enc", "rb") as f:
    cipher = f.read()

decrypted_text = []

for byte in cipher:
    libc.srand(seed)
    r = byte ^ (libc.rand() % 256)
    decrypted_text.append(chr(r))
    seed = byte

print("".join(decrypted_text))
```

# Flag
`shellmates{n0Th1nG_b3tT3r_th4N_4_cL455y_3NcrYpt0r}`