T = int(input())
answer = []
for _ in range(T):
    M, N, K = map(int, input().split())
    maps = set([ '_'.join(input().split())  for _ in range(K)])
    dic = dict()
    d = [[-1,0], [0,1], [1,0], [0,-1]]
    cnt = 0
    stack = []
    
    while maps:
        if len(stack):
            m = stack.pop()
        else:
            m = maps.pop()
        if dic.get(m) == None:
            dic[m] = cnt
            cnt += 1
        x, y = map(int, m.split("_"))
        for dy, dx in d:
            if f'{x+dx}_{y+dy}' in maps:
                dic[f'{x+dx}_{y+dy}'] = dic[m]
                stack.append(f'{x+dx}_{y+dy}')
                maps.remove(f'{x+dx}_{y+dy}')
    answer.append(cnt)
    
for i in answer:
    print(i)