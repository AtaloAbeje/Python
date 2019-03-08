def find_max_area(matrix):
    row = len(matrix)
    column = len(matrix[0])

    heights = [0 for _ in range(column)]
    left = [0 for _ in range(column)]
    right = [column for _ in range(column)]
    max_area = 0

    for i in range(row):
        # compute height
        for j in range(column):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

        # compute left
        cur_left = 0
        for j in range(column):
            if matrix[i][j] == '1':
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1

        # compute right
        cur_right = column
        for j in range(column - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = column
                cur_right = j

        # compute area of height[j] at row i
        for j in range(column):
            max_area = max(max_area, (right[j] - left[j]) * heights[j])

    return max_area


matrix = [["1","0","1","0","0"],
        ["1","0","1","0","0"],
        ["1","1","1","1","0"],
        ["1","0","1","1","0"]]

result = find_max_area(matrix)
print(result)


''' OUTPUT:

matrix = [["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
result:
6
------------
matrix = [["1","0","1","0","0"],
        ["1","0","1","0","0"],
        ["1","1","1","1","0"],
        ["1","0","1","1","0"]]
result:
4

'''