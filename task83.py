def count_case(s):
    counts = {'upper': 0, 'lower': 0}
    for char in s:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
    return counts

s = input("Enter a string: ")
case_counts = count_case(s)
print(f"Number of upper and lower case characters: {case_counts}")
