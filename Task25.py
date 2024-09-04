def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        result = -result
    return result

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = multiply(a, b)
print(f"The product of {a} and {b} is {result}.")
