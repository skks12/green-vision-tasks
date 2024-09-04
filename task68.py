lst1 = [int(x) for x in input("Enter elements of the first list separated by spaces: ").split()]
lst2 = [int(x) for x in input("Enter elements of the second list separated by spaces: ").split()]

merged_lst = lst1.copy()
for item in lst2:
    merged_lst.append(item)

print(f"The merged list is: {merged_lst}")
