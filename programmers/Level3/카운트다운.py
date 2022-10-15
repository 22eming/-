def solution(target):
    answer = [0,0]
    single = list(range(1,21))
    extra = set([s*2 for s in single][10:] + [s*3 for s in single][6:])
    single.append(50)
    
    dp = [[float('inf'),float('inf')] for _ in range(target+1)]
    dp[0] = [0,0]
    
    for i in range(1, target+1):
        for s in single:
            if i >= s:
                dp[i] = min(dp[i], [dp[i-s][0]+1, dp[i-s][1]+1], key= lambda x: [x[0],-x[1]])
            else: break
        for e in extra:
            if i >= e:
                dp[i] = min(dp[i], [dp[i-e][0]+1, dp[i-e][1]], key= lambda x: [x[0],-x[1]])
            else: break
                      
    
    return dp

print(solution(120))