lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]

if lst == sorted(lst):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
