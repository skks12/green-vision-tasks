def histogram(numbers, bin_size):
    hist = {}
    for num in numbers:
        bin_value = (num // bin_size) * bin_size
        hist[bin_value] = hist.get(bin_value, 0) + 1
    return hist

numbers = [int(x) for x in input("Enter the set of numbers separated by spaces: ").split()]
bin_size = int(input("Enter the bin size: "))

histogram_dict = histogram(numbers, bin_size)
print(f"The histogram is: {histogram_dict}")
