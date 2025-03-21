def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Parameters:
    n (int): The number of initial natural numbers to square and add to the sum.
    
    Returns:
    int: The sum of squares of the first n natural numbers.
    """
    return sum(i**2 for i in range(1, n + 1))

# Example usage
n = 5
result = sum_of_squares(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}")
