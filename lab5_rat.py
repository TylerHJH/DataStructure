maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]

start_point = (0, 0)
end_point = (13, 14)
stack = [start_point]
path = []


def explore(i, j):
    if j != 0 and maze[i][j - 1] == 1:
        stack.append((i, j - 1))
    if i != 0 and maze[i - 1][j] == 1:
        stack.append((i - 1, j))
    if i != 13 and maze[i + 1][j] == 1:
        stack.append((i + 1, j))
    if j != 14 and maze[i][j + 1] == 1:
        stack.append((i, j + 1))


def move(i, j):
    if (i, j) != end_point:
        maze[i][j] = 2
        explore(i, j)
        pre_row = i
        pre_column = j
        row = stack[len(stack) - 1][0]
        column = stack[len(stack) - 1][1]
        if row == pre_row and column == pre_column:
            while maze[row][column] == 2:
                stack.pop()
                row = stack[len(stack) - 1][0]
                column = stack[len(stack) - 1][1]
            move(row, column)
        else:
            move(row, column)
    else:
        while len(stack):
            p = stack.pop()
            if maze[p[0]][p[1]] == 2:
                path.append(p)
        print(path[::-1])


move(start_point[0], start_point[1])
