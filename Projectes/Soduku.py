def solution(matrix):
    find = find_empty(matrix)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check(matrix, i, (row, col)):
            matrix[row][col] = i

            if solution(matrix):
                return True

            matrix[row][col] = 0

    return False
def check(matrix, num, pos):
    # Check row
    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if matrix[i][j] == num and (i,j) != pos:
                return False
    return True
def print_board(matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i != 0 :
            print("--------+-------+------")

        for j in range(len(matrix[i])):
            if j > 8 or j == 0 or j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=" ")
def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                return (i, j)  # row, col

    return None

# main() ---------------------
matrix =[[5,0,7,6,0,0,0,3,4],
         [2,0,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

print("\nOrgenal:")
print_board(matrix)
solution(matrix)

print("\nSolution:")
print_board(matrix)