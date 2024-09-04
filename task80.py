dict1 = {int(k): v for k, v in (input("Enter key-value pairs for the first dictionary separated by space (key value): ").split() for _ in range(int(input("Enter number of elements for dict1: "))))}
dict2 = {int(k): v for k, v in (input("Enter key-value pairs for the second dictionary separated by space (key value): ").split() for _ in range(int(input("Enter number of elements for dict2: "))))}

merged_dict = {**dict1, **dict2}

print(f"The merged dictionary is: {merged_dict}")
