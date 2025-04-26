import numpy as np

def find_common_elements(lst1, lst2):
    """
    Find and return the common elements in two lists.
    
    Parameters:
    lst1 (list): The first list of items.
    lst2 (list): The second list of items.
    
    Returns:
    list: A list containing the common elements between lst1 and lst2.
    """
    return [element for element in lst1 if element in lst2]

# Example usage
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(find_common_elements(lst1, lst2))  # Output: [4, 5]
