rows = int(input("Enter the number of rows: "))
matrix = []

print("Enter the matrix elements row by row:")
for i in range(rows):
    matrix.append([int(x) for x in input().split()])

max_items = [max(row) for row in matrix]

print(f"The maximum item in each row is: {max_items}")
