def dfs(N:list, M, que:list):
    if len(N) == M:
        return N
    
    for i in range(len(que)):
        result = dfs(N+[que[i]], M, que[:i]+que[i+1:])
        if result != None:
            print(' '.join(result))
    

def main():
    N, M = map(int, input().split())
    que = list(map(str,range(1, N+1)))
    dfs([], M, que)
    
main()
    