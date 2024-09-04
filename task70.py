rows = int(input("Enter the number of rows: "))
matrix = []
print("Enter the matrix elements row by row:")

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

flattened_list = [item for sublist in matrix for item in sublist]

print(f"The 1D list is: {flattened_list}")
