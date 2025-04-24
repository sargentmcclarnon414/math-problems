import random

def generate_math_problem():
    """
    This function generates a random mathematical problem.
    The problem can be arithmetic, algebraic, or geometric.
    
    Returns:
        str: A randomly generated math problem statement.
    """
    operators = ['+', '-', '*', '/']
    numbers = [random.randint(-10, 10) for _ in range(3)]
    operation = random.choice(operators)
    problems = [
        f"Given the numbers {numbers}, solve this equation: {operation} ({numbers[0]} + {numbers[1]}) / {numbers[2]}.",
        "Find the value of x in the following problem: 2x - 5 = 10.",
        "Calculate the area of a rectangle with length 'l' and width 'w', where 'l' and 'w' are positive numbers."
    ]
    return random.choice(problems)

if __name__ == "__main__":
    print(generate_math_problem())
