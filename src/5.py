import random

def get_random_math_problem(upper_bound=100):
    """Generates a random math problem with two variables and an operator (+, -, x, /)."""
    variable1 = random.randint(1, upper_bound)
    variable2 = random.randint(1, upper_bound)
    operator = ['+', '-', 'x', '/'][random.randint(0, 3)]
    answer = eval(f"{variable1} {operator} {variable2}")
    return f"What is {variable1} {operator} {variable2}?"