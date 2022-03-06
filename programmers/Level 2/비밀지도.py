def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        data1 = bin(arr1[i])[2:]
        data2 = bin(arr2[i])[2:]

        # print(data1, data2)

        if len(data1) < n:
            length = n - len(data1)
            data1 = (length * '0') + data1

        if len(data2) < n:
            length = n - len(data2)
            data2 = (length * '0') + data2

        # print(data1, data2)

        string = ""
        for i in range(n):

            if data1[i] == '1' or data2[i] == '1':
                string = string + "#"
            else:
                string = string + " "

        answer.append(string)
    print(answer)
    return answer