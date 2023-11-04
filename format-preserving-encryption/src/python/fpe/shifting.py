"""
Implements the Shifting Numbers approach.
"""

class Shift:
    def __init__(self, n: int):
        if n < 1:
            raise ValueError("n must be > 0")
        
        self.n = n

    
    def map(self, i: int) -> int:
        if i < 0 or i >= self.n:
            raise ValueError("i must be >= 0 and < n")
        
        for round in range(2, self.n // 2):
            if (i + 1) % round == 0:
                i += round
                if i > self.n:
                    i = round - 1

        return i


def main():
    N = 10_000
    shift = Shift(N)

    for i in range(N):
        print(shift.map(i))


if __name__ == "__main__":
    main()
