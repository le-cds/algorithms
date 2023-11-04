from generators import offset, random_digits, random_number

for i in range(1000):
    number, iterations = random_number.generate_number(6)
    print(F"Generated {number} in {iterations} iterations")
