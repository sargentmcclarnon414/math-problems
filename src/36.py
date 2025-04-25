import math

def calculate_area_rectangle(length, width):
    area = length * width
    return area

def find_max_prime_number(n):
    max_prime = 0
    current_prime = 2
    while current_prime <= n:
        if all(current_prime % i != 0 for i in range(2, int(math.sqrt(current_prime)) + 1)):
            max_prime = current_prime
        current_prime += 1
    return max_prime

print(calculate_area_rectangle(length=5, width=3))
find_max_prime_number(n=100)
