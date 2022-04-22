def solution(s):
    data = list(map(int, s.split(" ")))
    answer = str(min(data))+ " " + str(max(data))
    print(answer)
    return answer