def solution(words, queries):
    answer = []

    for query in queries:
        count = 0
        for word in words:
            if len(word) != len(query):
                continue

            flag = True
            for i in range(len(word)):

                if query[i] == "?":
                    continue

                if word[i] != query[i]:
                    flag = False

            if flag:
                count += 1
        answer.append(count)
    return answer
