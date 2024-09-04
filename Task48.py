x = float(input("Enter the value of x: "))
sum_series = 0

for i in range(1, 8):
    term = ((-1) ** (i + 1)) * (x ** i) / i
    sum_series += term

print(f"The sum of the series is: {sum_series:.5f}")
