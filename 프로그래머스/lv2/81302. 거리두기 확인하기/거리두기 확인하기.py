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