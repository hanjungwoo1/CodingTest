from itertools import permutations


def isprime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    val = [list(permutations(numbers, i)) for i in range(1, len(numbers) + 1)]

    num = set()
    for x in val:
        for k in x:
            data = int("".join(k))
            if isprime(data):
                num.add(data)
    print(num)
    return len(num)