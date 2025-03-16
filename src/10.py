import random

def get_random_math_problem():
    """Generates a random math problem."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        return f"{num1} {op} {num2}"
    elif op == "-":
        return f"{num1} - {num2}"
    elif op == "*":
        return f"{num1} * {num2}"
    else:
        return f"{num1} / {num2}"
