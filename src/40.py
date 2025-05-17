import random

def print_random_string(length: int) -> str:
    """
    Generates a random string of given length.
    
    Example usage:
    >>> print_random_string(5)
    'GjyAa'
    """
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

# Example calls to the function
random_string = print_random_string(10)  # Randomly generate a string with 10 characters
print(random_string)
