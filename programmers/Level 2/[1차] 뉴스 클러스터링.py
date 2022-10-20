from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    left_length = len(str1)
    right_length = len(str2)

    left = []
    right = []

    for i in range(left_length - 1):
        temp = str1[i:i + 2]

        if temp.isalpha():
            left.append(temp)

    for i in range(right_length - 1):
        temp = str2[i:i + 2]

        if temp.isalpha():
            right.append(temp)

    Counter1 = Counter(left)
    Counter2 = Counter(right)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

    return answer