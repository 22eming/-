from collections import defaultdict

s_ddict = defaultdict(list)
e_ddict = defaultdict(list)
n, M = map(int, input().split())
for m in range(M):
    s, e = map(int, input().split())
    s_ddict[s].append(e)
    e_ddict[e].append(s)

result = []
stack = []
i = 1
while len(result) < n:
    # 선행 없
    if i not in e_ddict:
        if i not in result:
            result.append(i)
            for j in s_ddict[i]:
                e_ddict[j].remove(i)
                if e_ddict[j] == []:
                    del(e_ddict[j])
                    
        i += 1
        
    # 선행이 있다면
    elif i in e_ddict:
        i = e_ddict[i][0]
            
print(' '.join(list(map(str, result))))
