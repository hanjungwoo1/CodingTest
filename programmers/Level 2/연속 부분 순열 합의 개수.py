def solution(elements):
    new_elements = elements * 2

    result = set()

    for i in range(1, len(elements) + 1):
        for j in range(len(new_elements) - i + 1):
            temp = new_elements[j:j + i]
            result.add(sum(temp))

    return len(result)