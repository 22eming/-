def solution(places):
    answer = []
    for room in places:
        p = [[y, x]for y in range(5)
             for x in range(5) if room[y][x] == 'P']
        p.sort()
        for i in range(len(p)-1):
            for j in range(i+1, len(p)):
                t1, t2 = p[i], p[j]
                distance = abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])
                if distance == 1:
                    break
                elif distance == 2:
                    if t1[1] == t2[1]:  # x값이 같은지
                        if room[t1[0]+1][t1[1]] != 'X':
                            break
                    elif t1[0] == t2[0]:  # y값이 같은지
                        if room[t1[0]][t1[1]+1] != 'X':
                            break
                    else:
                        if t2[1] < t1[1]:
                            if room[t1[0]][t2[1]] != 'X' or room[t2[0]][t1[1]] != 'X':
                                break
                        else:
                            if room[t2[0]][t1[1]] != 'X' or room[t1[0]][t2[1]] != 'X':
                                break
            else:
                continue
            answer.append(0)
            break
        else:
            answer.append(1)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))

# 맨해튼 거리  (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2|
