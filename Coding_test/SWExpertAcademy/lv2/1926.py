for i in range(1, int(input())+1):
    answer = ''
    for x in str(i):
        if x in ['3', '6', '9']:
            answer += '-'
    print(answer if answer else i, end=' ')
