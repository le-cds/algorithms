"""
This solution generates n-digit numbers completely at random. It then checks whether the
number is readable or not. If it isn't, rinse and repeat until we have a readable number.
"""

import random


def _is_readable(n: str) -> bool:
    """
    Checks whether the given string representing a number is readable or not. It is readable
    if it does not contain digits that occur more than twice in succession.
    """
    for i in range(2, len(n)):
        if n[i - 2] == n[i - 1] and n[i - 1] == n[i]:
            return False

    return True


def generate_number(length: int) -> (str, int):
    iterations = 0

    max = 10 ** length
    result = "000000"

    while not _is_readable(result):
        iterations += 1

        number = random.randrange(max)
        result = str(number).rjust(length, '0')
    
    return (result, iterations)
