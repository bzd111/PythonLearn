# coding: utf-8
from pprint import pprint


def initMaze():
    maze = [[0] * 7 for _ in range(7)]
    walls = [
        (1, 3),
        (2, 1), (2, 5),
        (3, 3), (3, 4),
        (4, 2),  # (4, 3),
        (5, 4)
    ]
    for i in range(7):
        maze[0][i] = maze[i][-1] = 1
        maze[-1][i] = maze[i][0] = 1
    for i, j in walls:
        maze[i][j] = 1
    return maze


def run(maze, start, end):
    starti, startj = start
    endi, endj = end
    stack = [(starti, startj)]
    maze[starti][startj] = 1
    while stack:
        i, j = stack[-1]
        if (i, j) == end:
            break
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nowi = i + x
            nowj = j + y
            if maze[nowi][nowj] == 0:
                maze[nowi][nowj] = 1
                stack.append((nowi, nowj))
                break
        else:
            stack.pop()
    return stack

maze = initMaze()
pprint(maze)

pprint(run(maze, (1, 1), (5, 5)))
# [[1, 1, 1, 1, 1, 1, 1],
#  [1, 0, 0, 1, 0, 0, 1],
#  [1, 1, 0, 0, 0, 1, 1],
#  [1, 0, 0, 1, 1, 0, 1],
#  [1, 0, 1, 0, 0, 0, 1],
#  [1, 0, 0, 0, 1, 0, 1],
#  [1, 1, 1, 1, 1, 1, 1]]
# [(1, 1),
#  (1, 2),
#  (2, 2),
#  (3, 2),
#  (3, 1),
#  (4, 1),
#  (5, 1),
#  (5, 2),
#  (5, 3),
#  (4, 3),
#  (4, 4),
#  (4, 5),
#  (5, 5)]
