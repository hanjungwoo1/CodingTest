def solution(s):
    answer = 10000

    # 문자열의 절반정도 까지 반복
    for n in range(1, len(s) // 2 + 2):
        remain = ''         # 저장할 String
        count = 1
        temp = s[:n]

        for i in range(n, len(s) + n, n):
            if temp == s[i:i + n]:
                count += 1
            else:
                if count == 1:
                    remain += temp
                else:
                    remain += str(count) + temp
                temp = s[i:i + n]
                count = 1
        answer = min(answer, len(remain))

    return answer