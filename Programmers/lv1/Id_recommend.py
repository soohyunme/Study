def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4
    answer = answer.strip('.')

    # 5
    if answer == '':
        answer = 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')

    # 7
    while len(answer) <= 2:
        answer += answer[-1]
    return answer