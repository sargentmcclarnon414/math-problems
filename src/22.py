def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [3, 4, 7, 8, 9, 10]
results = []

for num in numbers:
    results.append(is_prime(num))

print(results)
