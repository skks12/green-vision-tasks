string = input("Enter a string: ")
char = input("Enter the character to find its index position: ")

positions = [index for index, c in enumerate(string) if c == char]

if positions:
    print(f"The character '{char}' is found at positions: {positions}")
else:
    print(f"The character '{char}' is not found in the string.")
