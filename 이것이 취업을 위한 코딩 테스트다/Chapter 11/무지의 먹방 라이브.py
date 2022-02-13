def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    answer = 0

    legth = len(food_times)

    param = 0
    count = 0
    while True:
        param = param % legth

        if food_times[param] > 0:
            food_times[param] -= 1
            param += 1
            count += 1
        else:
            param += 1

        if count == k:
            param += 1
            param = param % legth
            break

    answer = param
    return answer