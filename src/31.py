def calculate_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
