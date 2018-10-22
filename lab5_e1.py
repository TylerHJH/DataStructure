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


stack = [(0, 0)]
end_point = (13, 14)


def move(row, column):
    if column != 14 and maze[row][column + 1] == 1:
        column += 1
        stack.append((row, column))
    elif row != 13 and maze[row + 1][column] == 1:
        row += 1
        stack.append((row, column))
    elif row != 0 and maze[row - 1][column] == 1:
        row -= 1
        if (row, column) == stack[len(stack) - 2]:
            stack.pop()
            maze[row + 1][column] = 2
        else:
            stack.append((row, column))
    elif column != 0 and maze[row][column - 1] == 1:
        column -= 1
        if (row, column) == stack[len(stack) - 2]:
            stack.pop()
            maze[row][column + 1] = 2
        else:
            stack.append((row, column))


