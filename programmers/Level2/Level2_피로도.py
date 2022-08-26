from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for dungeon in permutations([i for i in range(len(dungeons))]):
        fatigue = k
        cnt = 0
        for i in dungeon:
            if dungeons[i][0] <= fatigue:  # 피로도를 충족
                fatigue -= dungeons[i][1]
                cnt += 1
            else:
                answer = max(answer, cnt)
                break
        else:
            answer = max(answer, cnt)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
