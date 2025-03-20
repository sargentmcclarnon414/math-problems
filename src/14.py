import sympy as sp

def calculate_square_root(x):
    """
    This function calculates and returns the square root of x.
    
    Parameters:
    x (float): The number to find the square root of.
    
    Returns:
    float: The square root of x.
    """
    return sp.sqrt(x)

# Example usage
x = 16.0
sqrt_x = calculate_square_root(x)
print(f"The square root of {x} is {sqrt_x}")
