def solution(picks, minerals):
    answer = 0
    mineral_set = [[0, 0, 0] for _ in range(10)]
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[: sum(picks) * 5]

    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            mineral_set[i // 5][0] += 1
        elif minerals[i] == "iron":
            mineral_set[i // 5][1] += 1
        else:
            mineral_set[i // 5][2] += 1

    mineral_set.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for index in range(len(mineral_set)):
        d, i, s = mineral_set[index]
        if index < picks[0]:
            answer += d + i + s
        elif index < picks[1] + picks[0]:
            answer += 5 * d + i + s
        else:
            answer += 25 * d + 5 * i + s
    return answer