def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + (rate / (n * 100))) ** (n * time)
    compound_interest = amount - principal
    return compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

ci = calculate_compound_interest(principal, rate, time, n)
print(f"The Compound Interest is: {ci}")
