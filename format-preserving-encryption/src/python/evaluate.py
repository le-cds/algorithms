import time

from fpe import ff3cipher, ring, shifting, thorp


N = 1_000_000
INVOCATIONS = 10_000


def measure(invocations: int, func) -> float:
    start = time.time()

    for i in range(invocations):
        func(i)
    
    end = time.time()
    return (end - start) / invocations


def measure_ff3() -> float:
    ff3_key = ff3cipher.generate_key()
    ff3_tweak = ff3cipher.generate_tweak()
    ff3 = ff3cipher.FF3Shuffle(N, ff3_key, ff3_tweak)

    return measure(INVOCATIONS, lambda i: ff3.map(i))


def measure_zring() -> float:
    zring = ring.ZRing(628_402, 328_935, 1_000_003, N)

    return measure(INVOCATIONS, lambda i: zring.map(i))


def measure_shifting() -> float:
    shift = shifting.Shift(N)

    return  measure(INVOCATIONS, lambda i: shift.map(i))


def measure_thorp() -> float:
    thorp_key = thorp.generate_key(128)
    thorp_shuffle = thorp.ThorpShuffle(N, 5_000, thorp_key)

    return measure(INVOCATIONS, lambda i: thorp_shuffle.map(i))


print(F"FF3: {measure_ff3()}")
print(F"ZRing: {measure_zring()}")
print(F"Shifting: {measure_shifting()}")
print(F"Thorp Shuffle: {measure_thorp()}")
