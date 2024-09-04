string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")

new_string = ''.join([char for char in string if char != char_to_remove])

print(f"The new string after removing '{char_to_remove}' is: {new_string}")
