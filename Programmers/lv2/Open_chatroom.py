def solution(record):
    answer = []
    user_info = {x.split()[1]: x.split()[2] for x in record if x.split()[0] != 'Leave'}
    _record = map(lambda x: x.split(), record)

    for x in _record:
        if x[0] == 'Leave':
            answer.append(user_info[x[1]] + '님이 나갔습니다.')
        elif x[0] == 'Enter':
            answer.append(user_info[x[1]] + '님이 들어왔습니다.')

    return answer