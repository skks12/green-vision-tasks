def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [int(x) for x in input("Enter list elements separated by spaces: ").split()]
sorted_lst = bubble_sort(lst)

print(f"The sorted list is: {sorted_lst}")
