def sum_of_squares_of_digits(a, b, c):
    return a**2 + b**2 + c**2

a = int(input("Enter the first digit: "))
b = int(input("Enter the second digit: "))
c = int(input("Enter the third digit: "))

result = sum_of_squares_of_digits(a, b, c)
print(f"The sum of the squares of the digits is: {result}")
