import random

def generate_math_problem():
    """
    Generate a random math problem.
    The problem will include addition, subtraction, multiplication,
    and division operations with integers between 1 and 9. The solution
    should be a fraction (a/b) in the form of int(a) / int(b).

    Returns:
        str: A randomly generated math problem.
    """
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    
    operation = random.choice(['+', '-'])
    if operation == '+':
        result = num1 + num2
    else:
        result = num1 * num2
    
    return f"{num1} {operation} {num2}", int(result)

problem = generate_math_problem()
print(problem)
