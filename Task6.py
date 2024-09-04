def is_odd_or_even(number):
    return "Even" if number % 2 == 0 else "Odd"

number = int(input("Enter a number: "))
print(f"The number is {is_odd_or_even(number)}.")
