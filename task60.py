lst = [int(x) for x in input("Enter the list elements separated by spaces: ").split()]
max_item = lst[0]

for item in lst:
    if item > max_item:
        max_item = item

print(f"The maximum item in the list is: {max_item}")
