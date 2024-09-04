def reverse_number(number):
    return str(number)[::-1]

number = input("Enter a number: ")
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}")
