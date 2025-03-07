import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Generate a random math operation (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])

    # Evaluate the problem
    result = eval(str(num1) + " " + op + " " + str(num2))

    return result
