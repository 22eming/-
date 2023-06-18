def conv_time(time : str):
    h, m = map(int, time.split(":"))
    return h*60 + m

def solution(plans):
    answer = []
    plans = sorted(plans, key=lambda x : [x[1]]) + [["null", "24:00", "0"]]
    stack = []
    for i in range(len(plans)-1):
        name, start, playtime = plans[i]
        extratime = (conv_time(plans[i+1][1]) - conv_time(start))
        if int(playtime) <= extratime:
            answer.append(name)
            extratime -= int(playtime)
            while stack:
                if stack[-1][1] <= extratime:
                    extratime -= stack[-1][1]
                    answer.append(stack.pop()[0])
                else:
                    stack[-1][1] -= extratime
                    break
        else:
            stack.append([name, int(playtime) - extratime])
    
    if stack:
        for i in range(-1, -len(stack)-1, -1):
            answer.append(stack[i][0])
    return answer