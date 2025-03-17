import random

def get_random_math_problem():
    """Return a random math problem."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operands = ['+', '-', '*', '/']
    number_1 = random.choice(numbers)
    number_2 = random.choice(numbers)
    operator = random.choice(operands)
    problem = f'{number_1} {operator} {number_2}'
    solution = eval(problem)
    return problem, solution
