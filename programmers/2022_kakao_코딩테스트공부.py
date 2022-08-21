from math import inf

def solution(alp, cop, problems):
    # 필요 최대 알고력, 코딩력
    max_a = max(problems, key = lambda x : x[0])[0]
    max_c = max(problems, key = lambda x : x[1])[1]
    # 알고 공부, 코딩 공부 케이스 추가
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    # 초기 값 인덱스 에러 방지
    if alp > max_a: alp = max_a
    if cop > max_c: cop = max_c

    # dp 선언
    dp =[ [inf]*(max_c+1) for _ in range(max_a+1) ]
    dp[alp][cop] = 0
    
    # 최대 학습을 넘었을 때 반영
    for i in range(alp, len(dp)):
        for j in range(cop, len(dp[0])):
            for problem in problems:
                req_a, req_c, a, c, t = problem
                if i >= req_a and j >= req_c:
                    if i + a < len(dp) and j + c < len(dp[0]):
                        dp[i+a][j+c] = min(dp[i+a][j+c], dp[i][j]+t)
                    elif j + c < len(dp[0]):
                        dp[-1][j+c] = min(dp[-1][j+c], dp[i][j]+t)
                    elif i + a < len(dp):
                        dp[i+a][-1] = min(dp[i+a][-1], dp[i][j]+t)
                    else:
                        dp[-1][-1] = min(dp[-1][-1], dp[i][j]+t)

    return dp[-1][-1]


alp, cop, problems = 10, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
print(solution(alp, cop, problems))