def solution(bridge_length, weight, truck_weights):
    wait, le, end, time = [], len(truck_weights), 0, []
    answer = 0
    while end != le:
        if time != []:
            if time[0] == 0:
                time.pop(0)
                wait.pop(0)
                end += 1

        if len(truck_weights) > 0: 
            if sum(wait) + truck_weights[0] <= weight:
                wait.append(truck_weights.pop(0))
                time.append(bridge_length)

        for n in range(len(time)):
            time[n] -= 1

        answer += 1

    return answer