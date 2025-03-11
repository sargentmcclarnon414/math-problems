import random

def get_random_math_problem(n):
    numbers = []
    operators = ["+", "-", "*", "/"]
    while len(numbers) < n:
        number = random.randint(1, 100)
        if number not in numbers:
            numbers.append(number)

    problem = " ".join([str(x) for x in numbers])
    problem += operators[random.randint(0, len(operators) - 1)]
    problem += str(numbers[n-1])

    return problem
