def solution(record):
    answer = []
    user = {}

    for data in record:
        data = data.split()
        if len(data) == 3:
            user[data[1]] = data[2]

    for data in record:
        data = data.split()
        if data[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % user[data[1]])
        if data[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % user[data[1]])
    return answer