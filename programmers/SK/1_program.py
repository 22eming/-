def solution(money, costs):
    answer = 0
    # 화폐 단위 / 생산 단가 : 생산 단가당 원
    cost = [1, 5, 10, 50, 100, 500]
    cost_re = []
    for i in range(6):
        cost_re.append([cost[i] / costs[i], cost[i]])
    cost_re.sort(reverse=True)

    dic = {1: 0, 5: 1, 10: 2, 50: 3, 100: 4, 500: 5}
    i = 0
    while money > 0:
        result = money // cost_re[i][1]
        if result > 0:
            answer += costs[dic[cost_re[i][1]]] * (result)
            money = money % cost_re[i][1]
        i += 1

    return answer


print(solution(1999,	[2, 11, 20, 100, 200, 600]))
