from typing import Counter

def solution(weights, head2head):
    answer = []

    for i in range(len(weights)):
        win_point = 0
        cnt = 0
        heavy_point = 0
        for n, j in enumerate(head2head[i]):
            if j != "N":
                cnt += 1
                if j == "W":
                    win_point += 1
                    if weights[i] < weights[n]:
                        heavy_point += 1
        if cnt == 0:
            win_point = 0
        else:
            win_point = win_point / (win_point + cnt)

        answer.append([win_point, heavy_point, weights[i], -(i+1) ])

    answer.sort(reverse=True)
    result = []
    for i in answer:
        result.append(-i[3])

    return result
print(solution([50,82,75,120,75],	["NLWLW","WNLLL","LWNWN","WWLNL","LWNWN"]))