def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        count = 0
        for i, s in enumerate(tree):
            if s in skill:
                if skill[count] != s:
                    break
                else:
                    count += 1
        else:
            answer += 1
    return answer