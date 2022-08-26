def solution(bridge_length, weight, truck_weights):
    wait, time, answer = [], [], 0
    truck_weights.reverse()

    while time != [] or answer == 0 or truck_weights != []:
        if truck_weights != []:
            if sum(wait) + truck_weights[-1] <= weight:
                answer += 1
                wait.append(truck_weights.pop())
                time.append(bridge_length)
                time = [i-1 for i in time]
                if time[0] == 0: del time[0]; del wait[0]
            else:
                answer += time[0]
                time = [i - time[0] for i in time]
                for i in time:
                    if i == 0:
                        del wait[0]
                time.remove(0)
        else:
            answer += time[-1]
            break

    return answer+1

# def solution(bridge_length, weight, truck_weights):
#     wait, le, end, time = [], len(truck_weights), 0, []
#     answer = 0
#     while end != le:
#         if time != []:
#             if time[0] == 0:
#                 time.pop(0)
#                 wait.pop(0)
#                 end += 1

#         if len(truck_weights) > 0: 
#             if sum(wait) + truck_weights[0] <= weight:
#                 wait.append(truck_weights.pop(0))
#                 time.append(bridge_length)

#         for n in range(len(time)):
#             time[n] -= 1

#         answer += 1

#     return answer



    
print(solution(1,10,[1,1,1,1,1,1,1,1,1,1,1,1]))
