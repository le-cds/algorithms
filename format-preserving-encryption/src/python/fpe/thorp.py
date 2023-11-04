"""
Implements the Thorp Shuffle approach.
"""

import re
import secrets


class ThorpShuffle:
    def __init__(self, n: int, rounds: int, hex_key: str):
        if n % 2 != 0:
            raise ValueError("n must be even.")
    
        if rounds < 1:
            raise ValueError("rounds must be > 0")
        
        if not re.fullmatch("([0-9a-f][0-9a-f])+", hex_key, flags=re.IGNORECASE):
            raise ValueError("key must consist of an even number of hex digits")
        
        self.n = n
        self.rounds = rounds
        self.key = int(hex_key, 16)
        self.key_length = len(hex_key) * 4
    

    def map(self, i: int) -> int:
        if i < 0 or i >= self.n:
            raise ValueError("i must be between 0 and n - 1.")
        
        N_HALF = self.n // 2

        for _ in range(self.rounds):
            # Find where our i is in its half of the current stack of n cards
            half = 0
            pos_in_half = i
            if i >= N_HALF:
                half = 1
                pos_in_half -= N_HALF
            
            # Find the appropriate bit in our key
            bit_pos = pos_in_half % self.key_length
            bit = ((1 << bit_pos) & self.key) >> bit_pos

            # The bit determines which half (left = 0, right = 1) comes first. Whether our
            # card comes first is determined by whether its half matches the bit
            offset = half ^ bit
            i = pos_in_half * 2 + offset

        return i
        

def generate_key(nbytes: int) -> str:
    return secrets.token_hex(nbytes)


def main():
    N = 10_000
    shuffle = ThorpShuffle(N, 2_000, generate_key(128))

    for i in range(N):
        print(shuffle.map(i))


if __name__ == "__main__":
    main()
