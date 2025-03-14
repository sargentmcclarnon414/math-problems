import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def solve_math_problem():
    min_value = 1
    max_value = 10
    problem_type = "addition"
    
    # Generate a random number within the specified range
    number = get_random_number(min_value, max_value)
    
    # Generate a random operator (e.g. +, -, x, /)
    operator = ["+", "-", "*", "/"][random.randint(0, 3)]
    
    # Generate a second random number within the specified range
    number2 = get_random_number(min_value, max_value)
    
    # Solve the problem using the chosen operator
    if problem_type == "addition":
        answer = number + number2
    elif problem_type == "subtraction":
        answer = number - number2
    elif problem_type == "multiplication":
        answer = number * number2
    else:  # division
        answer = number / number2
    
    return answer
