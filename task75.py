def can_multiply(mat1, mat2):
    return len(mat1[0]) == len(mat2)

rows1 = int(input("Enter the number of rows for the first matrix: "))
print("Enter the first matrix:")
mat1 = [list(map(int, input().split())) for _ in range(rows1)]

rows2 = int(input("Enter the number of rows for the second matrix: "))
print("Enter the second matrix:")
mat2 = [list(map(int, input().split())) for _ in range(rows2)]

if can_multiply(mat1, mat2):
    print("Matrix multiplication is possible.")
else:
    print("Matrix multiplication is not possible.")
