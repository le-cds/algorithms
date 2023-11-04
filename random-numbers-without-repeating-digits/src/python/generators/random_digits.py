"""
This solution generates n-digit numbers digit by digit. A digit is re-generated if
it would occur more than twice in succession.
"""

import random


def generate_number(length: int) -> (str, int):
    result = ""
    iterations = 0

    last_digit = -1
    last_digit_count = 0

    while len(result) < length:
        iterations += 1

        new_digit = random.randrange(10)

        if new_digit == last_digit:
            if last_digit_count < 2:
                result += str(new_digit)

                last_digit_count += 1
        
        else:
            result += str(new_digit)

            last_digit = new_digit
            last_digit_count = 1

    return (result, iterations)
