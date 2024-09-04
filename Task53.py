string = input("Enter a string: ")
char = input("Enter the character to find its frequency: ")
frequency = 0

for c in string:
    if c == char:
        frequency += 1

print(f"The frequency of '{char}' in the string is: {frequency}")
