import numpy as np

def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence of length n.
    
    Parameters:
    - n: int, the length of the Fibonacci sequence to generate
    
    Returns:
    - list: A Fibonacci sequence of length n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

# Example usage
n = 10
fibonacci_sequence(n)
