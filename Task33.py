def calculate_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def calculate_lcm(x, y):
    hcf = calculate_hcf(x, y)
    lcm = (x * y) // hcf
    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = calculate_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}")
