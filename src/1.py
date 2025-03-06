import random

def get_math_problem(max_value):
    operator = random.choice(['+', '-', '*', '/'])
    problem = f"{random.randint(1, max_value)} {operator} {random.randint(1, max_value)}"
    return problem