lst = [int(x) for x in input("Enter the list elements separated by spaces: ").split()]
unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print(f"The list after removing duplicates: {unique_lst}")
