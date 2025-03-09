import random

def get_random_math_problem(n):
    numbers = [random.randint(1, n) for i in range(2)]
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    return f"{numbers[0]} {operator} {numbers[1]}"
