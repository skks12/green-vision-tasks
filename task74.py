rows = int(input("Enter the number of rows: "))
matrix = []

print("Enter the matrix elements row by row:")
for i in range(rows):
    matrix.append([int(x) for x in input().split()])

shape = (rows, len(matrix[0]) if matrix else 0)
print(f"The shape of the matrix is: {shape}")
