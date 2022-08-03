def solution(rows, columns, queries):
    table = []
    answer = []

    for r in range(rows):
        table.append([x for x in range(r * columns + 1, (r + 1) * columns + 1)])

    for x1, y1, x2, y2 in queries:
        min_val = table[x1 - 1][y2 - 1]

        tmp = table[x1 - 1][y2 - 1]
        for i in range(y2, y1, -1):
            min_val = min(min_val, table[x1 - 1][i - 2])
            table[x1 - 1][i - 1] = table[x1 - 1][i - 2]

        for i in range(x1, x2):
            tmp, table[i][y2 - 1] = table[i][y2 - 1], tmp
            min_val = min(min_val, tmp)

        for i in range(y2 - 2, y1 - 2, -1):
            tmp, table[x2 - 1][i] = table[x2 - 1][i], tmp
            min_val = min(min_val, tmp)

        for i in range(x2 - 2, x1 - 2, -1):
            tmp, table[i][y1 - 1] = table[i][y1 - 1], tmp
            min_val = min(min_val, tmp)

        answer.append(min_val)

    return answer