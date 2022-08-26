from itertools import combinations


def solution(relation):
    answer = []
    lenth = len(relation[0])
    relations = [i for i in range(lenth)]
    for i in range(1, lenth + 1):
        for j in combinations(relations, i):
            # 최소성 검사
            if [1 for m in answer if set(m).issubset(set(j))]:
                continue

            s = []
            # 모든 행 검사
            for k in range(len(relation)):
                # 특정 열 추출
                rel = [relation[k][l] for l in j]
                # 유일성 판별
                if rel not in s:
                    s.append(rel)
            if len(s) == len(relation):
                answer.append(j)
    return len(answer)


print(solution([["a", "aa"], ["aa", "a"], ["a", "a"]]))
