def solution(N, stages):
    ros, n = [], len(stages)
    for idx, i in enumerate(range(1,N+1)):
        ros += [[stages.count(i) / n , idx]]
        n -= stages.count(i)
        if n == 0 and idx != N-1:
            for i in range(idx+1,N):
                ros += [[0,i]]
            break
    a = sorted(ros, reverse = True, key= lambda x: (x[0], -x[1]))
    return [n[1]+1 for n in a]