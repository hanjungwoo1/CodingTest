from itertools import combinations

def solution(relations):
    row, col = len(relations), len(relations[0])
    candidates = []

    for i in range(1, col + 1):
        candidates.extend(combinations([x for x in range(col)], i))

    unique = []
    for candidate in candidates:
        temp = [tuple([relation[i] for i in candidate]) for relation in relations]

        if len(set(temp)) == row:
            check = True
            for u in unique:
                if set(u).issubset(set(candidate)):
                    check = False
                    break
            if check:
                unique.append(candidate)

    return len(unique)