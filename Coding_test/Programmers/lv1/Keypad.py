def cal_pos(c, MAP, hand, left, right):
    left_pos = MAP[left]
    right_pos = MAP[right]
    num_pos = MAP[c]
    left_diff = abs(left_pos[0] - num_pos[0]) + abs(left_pos[1] - num_pos[1])
    right_diff = abs(right_pos[0] - num_pos[0]) + abs(right_pos[1] - num_pos[1])
    if left_diff == right_diff:
        if hand == 'right':
            return True
        return False
    elif right_diff < left_diff:
        return True
    return False


def solution(numbers, hand):
    answer = ''
    MAP = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
           '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left_hand = '*'
    right_hand = '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_hand = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right_hand = num
        else:
            if cal_pos(num, MAP, hand, left_hand, right_hand):
                answer += 'R'
                right_hand = num
            else:
                answer += 'L'
                left_hand = num

    return answer