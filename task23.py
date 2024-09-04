def swap_numbers(a, b):
    return b, a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = swap_numbers(a, b)

print(f"After swapping: first number = {a}, second number = {b}")
