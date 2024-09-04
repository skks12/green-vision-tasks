list1 = [int(x) for x in input("Enter elements of the first list separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter elements of the second list separated by spaces: ").split()]

union_list = list(set(list1) | set(list2))
intersection_list = list(set(list1) & set(list2))

print(f"Union of the lists: {union_list}")
print(f"Intersection of the lists: {intersection_list}")
