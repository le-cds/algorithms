"""
Evaluates the different random number generators by checking how many iterations they
will use to produce their numbers.
"""

from generators import offset, random_digits, random_number


NUMBER_OF_DIGITS = 6
TEST_RUNS = 1_000_000


def _test_generator(generator) -> list[int]:
    required_iterations = []

    for _ in range(TEST_RUNS):
        _, iterations = generator(NUMBER_OF_DIGITS)
        required_iterations.append(iterations)

    return required_iterations


def _evaluate(generator_name: str, generator):
    required_iterations = _test_generator(generator)
    max_required_iterations = max(required_iterations)

    histogram = [0] * (max_required_iterations + 1)
    for iterations in required_iterations:
        histogram[iterations] += 1

    print(generator_name)
    print("-" * len(generator_name))

    for iterations in range(len(histogram)):
        if histogram[iterations] > 0:
            percentage = histogram[iterations] / TEST_RUNS * 100
            percentage_string = "{:.2f}".format(percentage).rjust(6)
            print(F"{str(iterations).rjust(3)}: {percentage_string}%")
    
    print()


_evaluate("Offset Algorithm", offset.generate_number)
_evaluate("Random Digits Algorithm", random_digits.generate_number)
_evaluate("Randum Number Algorithm", random_number.generate_number)
