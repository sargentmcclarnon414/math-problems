import math

def calculate_sum(numbers):
    """
    This function takes a list of numbers and returns their sum.
    Example usage:
    >>> calculate_sum([1, 2, 3])
    6
    >>> calculate_sum([-1, -2, -3])
    -6
    """
    return sum(numbers)

# A random integer for testing purposes
test_case = [10, 20, 30]
random_result = calculate_sum(test_case)
print(random_result)
