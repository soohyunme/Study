def solution(N, stages):
    stages.sort()
    clear_user_num = [0] * N
    fail_user_num = [0] * N
    for i in range(len(stages)):
        if stages[i] > N:
            break
        fail_user_num[stages[i] - 1] += 1

    count = len(stages)
    for i, fail_count in enumerate(fail_user_num):
        clear_user_num[i] = count
        count -= fail_count

    fail_ratio = [i / j if j != 0 else 0 for i, j in zip(fail_user_num, clear_user_num)]
    answer = [(ratio, i) for i, ratio in enumerate(fail_ratio)]
    answer.sort(key=lambda x: (-x[0], x[1]))
    return list(map(lambda x: x[1] + 1, answer))