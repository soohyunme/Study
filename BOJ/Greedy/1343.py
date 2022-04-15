import sys
In = sys.stdin.readline

board = In()

answer = ''

while True:
    if board[0] == '.':
        answer += '.'
        board = board[1:]
    elif board[0:4] == 'XXXX':
        answer += 'AAAA'
        board = board[4:]
    elif board[0:2] == 'XX':
        answer += 'BB'
        board = board[2:]
    else:
        if len(board) != 1:
            answer = '-1'
        break
print(answer)

