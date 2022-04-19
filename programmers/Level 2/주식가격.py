def solution(prices):
    N = len(prices)
    answer = []
    for i, data in enumerate(prices):
        # print("!!", data, "!!")
        count = 0
        for j in range(i + 1, N):
            # print(j, prices[j])
            if data > prices[j]:
                count += 1
                break
            else:
                count += 1
        answer.append(count)
    return answer



