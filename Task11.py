def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
interest = simple_interest(principal, rate, time)
print(f"The simple interest is: {interest:.2f}")
