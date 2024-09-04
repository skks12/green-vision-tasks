def reverse_number(number):
    return int(str(number)[::-1])

number = int(input("Enter a four-digit number: "))
reversed_number = reverse_number(number)
print("The reversed number is:", reversed_number)
if number == reversed_number:
    print("The reversed number is equal to the original number.")
else:
    print("The reversed number is not equal to the original number.")
