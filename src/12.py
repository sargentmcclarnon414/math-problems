import random

def get_random_math_problem(difficulty=1):
    numbers = list(range(0, 10))
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        result = num1 / num2
    return f"{num1} {operator} {num2} = {result}"
