import random

def generate_math_problem(n=1):
    """Generate a random math problem"""
    numbers = []
    operators = ['+', '-', '*', '/']
    for i in range(n):
        number = random.randint(1, 20)
        while number in numbers:
            number = random.randint(1, 20)
        numbers.append(number)
    operator = random.choice(operators)
    return f"{numbers[0]} {operator} {numbers[1]}"
