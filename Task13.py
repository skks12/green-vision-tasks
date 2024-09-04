def is_divisible_by_3_and_6(number):
    return number % 3 == 0 and number % 6 == 0

number = int(input("Enter a number: "))
if is_divisible_by_3_and_6(number):
    print(f"{number} is divisible by both 3 and 6.")
else:
    print(f"{number} is not divisible by both 3 and 6.")
