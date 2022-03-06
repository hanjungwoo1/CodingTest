def solution(progresses, speeds):
    days = []
    for i, j in zip(progresses, speeds):
        day = (100 - i) // j
        if ((100 - i) % j) > 0:
            day = day + 1

        days.append(day)

    print(days)
    max = days[0]

    result = []
    count = 1
    del days[0]
    for x in days:
        if x <= max:
            count = count + 1
        else:
            max = x
            result.append(count)
            count = 1
    result.append(count)
    print(result)
    return result

# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer
