lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
squared_lst = [x**2 for x in lst]

print(f"The new list with squares is: {squared_lst}")
