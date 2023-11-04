"""
Implements the Z Ring approach.
"""

class ZRing:
    def __init__(self, a: int, b: int, p: int, n: int):
        if a < 1 or a >= p:
            raise ValueError("a must be >= 1 and < p")

        if p <= n:
            raise ValueError("p must be >= n")
        
        self.a = a
        self.b = b
        self.p = p
        self.n = n
        
    
    def map(self, i: int) -> int:
        if i < 0 or i >= self.n:
            raise ValueError("i must be >= 0 and < n")
        
        result = (self.a * i + self.b) % self.p
        while result >= self.n:
            result = (self.a * result + self.b) % self.p
        
        return result


def main():
    N = 10_000
    zring = ZRing(8_139, 5_781, 10_007, N)

    for i in range(N):
        print(zring.map(i))


if __name__ == "__main__":
    main()