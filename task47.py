x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
sum_series = 1

for i in range(2, n + 1):
    sum_series += x**i / i

print(f"The sum of the series is: {sum_series:.5f}")
