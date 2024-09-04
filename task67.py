lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
odd_lst = [x for x in lst if x % 2 != 0]
even_lst = [x for x in lst if x % 2 == 0]

print(f"Odd numbers list: {odd_lst}")
print(f"Even numbers list: {even_lst}")
