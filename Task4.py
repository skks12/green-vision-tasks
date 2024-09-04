def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

number = int(input("Enter a three-digit number: "))
print("The sum of the digits is:", sum_of_digits(number))
