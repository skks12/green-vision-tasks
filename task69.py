lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
old_item = int(input("Enter the item to replace: "))
new_item = int(input("Enter the new item: "))

for i in range(len(lst)):
    if lst[i] == old_item:
        lst[i] = new_item

print(f"The list after replacement: {lst}")
