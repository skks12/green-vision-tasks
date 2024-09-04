string = input("Enter a string: ")
words = string.split()

title_case_string = ' '.join([word.capitalize() for word in words])

print(f"The title case version of the string is: {title_case_string}")
