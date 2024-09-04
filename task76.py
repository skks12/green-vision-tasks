def multiply_matrices(mat1, mat2):
    result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

rows1 = int(input("Enter the number of rows for the first matrix: "))
print("Enter the first matrix:")
mat1 = [list(map(int, input().split())) for _ in range(rows1)]

rows2 = int(input("Enter the number of rows for the second matrix: "))
print("Enter the second matrix:")
mat2 = [list(map(int, input().split())) for _ in range(rows2)]

if len(mat1[0]) == len(mat2):
    result = multiply_matrices(mat1, mat2)
    print("The result of matrix multiplication is:")
    for row in result:
        print(row)
else:
    print("Matrix multiplication is not possible.")
