def add_numbers(x, y):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return x + y

def calculate_math_operations():
    """
    This function performs basic arithmetic operations with two given numbers.
    It can handle addition, subtraction, multiplication, and division.
    """
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Perform the operations
    result1 = add_numbers(a, b)
    operation_result = add_numbers(result1, a) / b if (operation_result := a + b) and (b := b - a) else result1

    print(f"The sum of {a} and {b} is: {result1}")
    print(f"Result of {add_numbers(a, b)} divided by {b} is: {operation_result}")

if __name__ == "__main__":
    calculate_math_operations()
