from LinkedQueue import Node
from LinkedQueue import LinkedQueue
from sys import stdin

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def rook_path(start_x, start_y, end_x, end_y, matrix):
    def check(x, y, matrix):
        if 0 <= x < 8 and 0 <= y < 8 and matrix[x][y] != "c" or matrix[x][y] == False:
            return True
        return False
    # visited set = 8 x 8 array of booleans
    # visited[x][y] is True if we have visited (x, y)
    #visited = [[False] * 8 for i in range(8)]

    q = LinkedQueue()
    q.enqueue((start_x, start_y, 0))
    matrix[start_x][start_y] = True

    while not q.isEmpty():
        x, y, dist = q.dequeue()
        if (x, y) == (end_x, end_y):
            print(dist)
            return
        x1 = x
        x1_ = x
        y1 = y
        y1_ = y
        check = False
        while (x1 < 8 and matrix[x1][y1] != 'x'):
            if 0 <= x1 < 8 and 0 <= y1 < 8 and (matrix[x1][y1] == False or matrix[x1][y1] == "c"):
                q.enqueue((x1, y1, dist + 1))
                matrix[x1][y1] = True
            x1 += 1
        x1 = x
        while (x1 >= 0 and matrix[x1][y1] != 'x'):
            if 0 <= x1 < 8 and 0 <= y1 < 8 and (matrix[x1][y1] == False or matrix[x1][y1] == "c"):
                q.enqueue((x1, y1, dist + 1))
                matrix[x1][y1] = True
            x1 -= 1
        x1 = x

        while (y1 < 8 and matrix[x1][y1] != 'x'):
            if 0 <= x1 < 8 and 0 <= y1 < 8 and (matrix[x1][y1] == False or matrix[x1][y1] == "c"):
                q.enqueue((x1, y1, dist + 1))
                matrix[x1][y1] = True
            y1 += 1
        y1 = y
        while (y1 >= 0 and matrix[x1][y1] != 'x'):
            if 0 <= x1 < 8 and 0 <= y1 < 8 and (matrix[x1][y1] == False or matrix[x1][y1] == "c"):
                q.enqueue((x1, y1, dist + 1))
                matrix[x1][y1] = True
            y1 -= 1
        y1 = y


    print('-1')


matrix = []
row = []

for line in stdin:
    for x in line.rstrip():
        if x == ".":
            row.append(False)
        elif x == "x":
            row.append("x")
        else:
            row.append(x)
    matrix.append(row)
    row = []


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "v":
            start_x = i
            start_y = j
        elif matrix[i][j] == "c":
            end_x = i
            end_y = j



rook_path(start_x, start_y, end_x, end_y, matrix)


