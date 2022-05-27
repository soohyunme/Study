def incorrect_puzzle(arr):
    if sorted(arr) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return 1
    return 0

def puzzle_check():
    table = [list(map(int, input().split())) for _ in range(9)]
    # row check
    for arr in table:
        if incorrect_puzzle(arr):
            return 0

    # column check
    for j in range(len(table)):
        arr = []
        for i in range(len(table)):
            arr.append(table[i][j])
        if incorrect_puzzle(arr):
            return 0

    # square check
    arr1, arr2, arr3 = [], [], []
    for i in range(len(table)):
        if i % 3 == 0:
            arr1, arr2, arr3 = [], [], []
        arr1.extend(table[i][0:3])
        arr2.extend(table[i][3:6])
        arr3.extend(table[i][6:])
        if i % 3 == 2:
            if incorrect_puzzle(arr1) or incorrect_puzzle(arr2) or incorrect_puzzle(arr3):
                return 0
    return 1


for _ in range(1, int(input())+1):
        print('#' + str(_), puzzle_check())
