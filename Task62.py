lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
number = int(input("Enter the number to search: "))

if number in lst:
    print(f"{number} is present in the list.")
else:
    print(f"{number} is not present in the list.")
