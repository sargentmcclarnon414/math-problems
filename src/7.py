import random

def get_random_math_problem(n=2):
    """Generate a random math problem with n variables."""
    variables = [f"x{i}" for i in range(1, n+1)]
    operations = ["+", "-", "*"]
    equation = "".join(random.choice(variables) + random.choice(operations) + str(random.randint(1, 10)) for _ in range(n-1))
    return f"{equation} = {random.randint(1, 10)}"
