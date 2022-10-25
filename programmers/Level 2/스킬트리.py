def check(skill_tree, skill):
    now = 0
    for s in skill_tree:
        if s in skill:
            if skill.index(s) == now:
                now += 1
            else:
                return False
    return True


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        if check(skill_tree, skill):
            answer += 1

    return answer