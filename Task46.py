import math

n = int(input("Enter the value of n: "))
sum_series = 0

for i in range(1, n + 1):
    sum_series += i / math.factorial(i)

print(f"The sum of the series is: {sum_series:.5f}")
