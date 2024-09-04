string = input("Enter a string: ")
words = string.split()
reversed_words = ' '.join(words[::-1])

print(f"The reversed word string is: {reversed_words}")
