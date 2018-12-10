def add_matrices(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            return mat1[i][j] + mat2[i][j]

mat1 = [[1,2],
        [3,4],
        [5,6]]
        
mat2 = [[5,6],
        [3,4],
        [1,2]]
mat3=[[]]

print("matrix 1:", mat1)
print("matrix 2:", mat2)
mat3 = add_matrices(mat1, mat2)

print("matrix 3:")
for i in range(len(mat2)):
    for j in  range(len(mat2[i])):
        print(mat3[i][j])

# pec.03 Answar 5 # Atalo Abeje