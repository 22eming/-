from collections import defaultdict

def sheep_to_wolf(info, node, p):
    # 리프일 때
    wolf, sheep = [], 0
    if p not in node:
        return [], sheep
    # 자식이 하나일때
    elif len(node[p]) == 1:
        if info[node[p][0]] == 0:
            w, s = sheep_to_wolf(info, node, node[p][0])
            wolf.extend(w)
            sheep += s+1
        else:
            wolf.append(node[p][0])
    # 자식이 둘
    else:
        # 늑대 추가
        for i in range(2):
            if info[node[p][i]] == 0:
                w, s = sheep_to_wolf(info, node, node[p][i])
                wolf.extend(w)
                sheep += 1 + s
            if info[node[p][i]] == 1:
                wolf.append(node[p][i])
    return wolf, sheep


def dfs(wolf, wolf_cnt, sheep, info, node, wolf_list):
    sheep_cnt = 0
    for i in range(len(wolf)):
        if wolf_cnt == sheep-1:
            return sheep
        w = wolf.pop(0)
        child_wolf, s = sheep_to_wolf(info, node, w)
        sheep_cnt = max(sheep_cnt, dfs(wolf+child_wolf, wolf_cnt+1, sheep+s, info, node, wolf_list+[w]))
        wolf.append(w)
    return max(sheep, sheep_cnt)


def solution(info, edges):
    answer = 0
    node = defaultdict(list)
    for p, c in edges:
        node[p].append(c)
    wolf, sheep = sheep_to_wolf(info, node, 0)
    print(node)
    answer = dfs(wolf, 0, sheep+1, info, node, [])
    return answer