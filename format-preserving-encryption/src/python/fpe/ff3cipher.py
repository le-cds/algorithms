"""
Implements the FF3 format-preserving encryption approach.
"""

import secrets
from ff3 import FF3Cipher


class FF3Shuffle:
    def __init__(self, n: int, key: str, tweak: str):
        if n < 1_000_000:
            raise ValueError("n must be >= 1.000.000")

        self.length = len(str(n-1))
        self.cipher = FF3Cipher(key, tweak)
    

    def map(self, i: int) -> int:
        i_str = str(i)
        i_str = i_str.rjust(self.length, "0")
        
        i_str = self.cipher.encrypt(i_str)

        return int(i_str)


def generate_key() -> str:
    return secrets.token_hex(16)


def generate_tweak() -> str:
    return secrets.token_hex(7)


def main():
    N = 1_000_000
    ff3 = FF3Shuffle(N, generate_key(), generate_tweak())
    
    for i in range(N):
        print(ff3.map(i))


if __name__ == "__main__":
    main()
