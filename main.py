import hashlib
import random

def make_rng(key):
    h = hashlib.sha256(key.encode("utf-8")).digest()
    seed = int.from_bytes(h, "big")

    return random.Random(seed)

def encrypt(text, key):
    rng = make_rng(key)
    data = text.encode("utf-8")
    out = []

    for b in data:
        r = rng.randint(0, 255)
        c = b ^ r
        c = c + rng.randint(0, 999)
        out.append(f"{c:04d}")

    return " ".join(out)

def decrypt(code_text, key):
    rng = make_rng(key)
    nums = code_text.split()
    data = bytearray()

    for n in nums:
        r = rng.randint(0, 255)
        c = int(n) - rng.randint(0, 999)
        b = c ^ r
        data.append(b & 0xFF)

    return data.decode("utf-8")

if __name__ == "__main__":
    key = input("K: ")
    text = input("T: ")

    enc = encrypt(text, key)
    print("\nE:")
    print(enc)

    dec = decrypt(enc, key)
    print("\nF-CvO. D:")
    print(dec)
