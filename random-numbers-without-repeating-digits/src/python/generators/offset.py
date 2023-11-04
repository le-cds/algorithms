"""
Generates n-digit numbers digit by digit. The way each digit is chosen prevents consecutive
runs of digits by design.
"""

import random


def generate_number(length: int) -> str:
    result = ""
    last_two_digits = [-1, -2]

    for i in range(length):
        if last_two_digits[0] == last_two_digits[1]:
            # The last two digits are the same; we need to generate a different digit next
            offset = last_two_digits[0] + 1
            digit = (random.randrange(9) + offset) % 10

        else:
            # The last two digits were different; we're free to generate any digit we like
            digit = random.randrange(10)

        # Alternate between the first and second list position for storing the new digit.
        # This very simply allows us to always remember the most recent two digits
        last_two_digits[i % 2] = digit

        result = result + str(digit)

    return result
