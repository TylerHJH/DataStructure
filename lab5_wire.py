maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
        [-1, -1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, -1, -1],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, -1, 0, 0, -1, -1, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0],
        [0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0]]

start_point = (4, 1)
end_point = (5, 4)
stack = [start_point]
path = []
pace = 0
maze[start_point[0]][start_point[1]] = 0
judgement = True


def explore(i, j, p):
    if j != 0 and maze[i][j - 1] == 0:
        stack.append((i, j - 1))
        maze[i][j - 1] = p
    if i != 0 and maze[i - 1][j] == 0:
        stack.append((i - 1, j))
        maze[i - 1][j] = p
    if i != 13 and maze[i + 1][j] == 0:
        stack.append((i + 1, j))
        maze[i + 1][j] = p
    if j != 14 and maze[i][j + 1] == 0:
        stack.append((i, j + 1))
        maze[i][j + 1] = p


def move():
    global judgement
    if judgement is True:
        global pace
        while maze[stack[0][0]][stack[0][1]] == pace:
            d = stack[0]
            del stack[0]
            if d != end_point:
                explore(d[0], d[1], pace + 1)
            else:
                path.append(d)
                row = end_point[0]
                column = end_point[1]
                while start_point != (row, column):
                    if column != 0 and maze[row][column - 1] == pace - 1:
                        path.append((row, column - 1))
                        column -= 1
                    if row != 0 and maze[row - 1][column] == pace - 1:
                        path.append((row - 1, column))
                        row -= 1
                    if row != 13 and maze[row + 1][column] == pace - 1:
                        path.append((row + 1, column))
                        row += 1
                    if column != 14 and maze[row][column + 1] == pace - 1:
                        path.append((row, column + 1))
                        column += 1
                    pace -= 1
                print(path[::-1])
                judgement = False
        pace += 1
        maze[start_point[0]][start_point[1]] = -2
        move()


move()


