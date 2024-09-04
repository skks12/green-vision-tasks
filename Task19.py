def is_narcissist_number(number):
    num_str = str(number)
    num_len = len(num_str)
    narcissist_sum = sum(int(digit) ** num_len for digit in num_str)
    return narcissist_sum == number

number = int(input("Enter a four-digit number: "))
if is_narcissist_number(number):
    print(f"{number} is a Narcissist number.")
else:
    print(f"{number} is not a Narcissist number.")
