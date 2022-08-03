def solution(brown, yellow):
    for i in range(3, brown):
        for j in range(3, brown):
            if (i-2) * (j-2) == yellow and i*j == brown+yellow:
                return [max(i, j), min(i, j)]