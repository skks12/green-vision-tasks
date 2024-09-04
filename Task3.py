def swap_numbers(a, b):
    return b, a

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1, num2 = swap_numbers(num1, num2)
print(f"After swapping: First number = {num1}, Second number = {num2}")
