def board_WB(array, x, y):
    count = 0
    for row in range(x, x+8):
        for col in range(y, y+8):
            if (row + col) % 2 == 0 and array[row][col] != 'W':
                count += 1
            elif (row + col) % 2 == 1 and array[row][col] != 'B':
                count += 1
    return count


def board_BW(array, x, y):
    count = 0
    for row in range(x, x+8):
        for col in range(y, y+8):
            if (row + col) % 2 == 0 and array[row][col] != 'B':
                count += 1
            elif (row + col) % 2 == 1 and array[row][col] != 'W':
                count += 1
    return count


n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(input())

answer = 64
for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, board_WB(board, i, j))
        answer = min(answer, board_BW(board, i, j))
print(answer)

