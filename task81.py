def swap_min_max(d):
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    
    d[min_key], d[max_key] = d[max_key], d[min_key]
    
    return d

d = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = swap_min_max(d)
print(f"The dictionary after swapping min and max values: {swapped_dict}")
