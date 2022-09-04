N = int(input())

data = []
for i in range(N): # 친구 입력
    temp = [idx for idx, j in enumerate(list(input())) if j == 'Y']
    data.append(temp)

answer = 0
for i in range(N): # 친구 계산 : 겹치는 친구
    cnt = set(data[i])
    for j in data[i]:
        for k in data[j]:
            if k != i:
                cnt.add(k)
    answer = max(answer, len(cnt))
    
print(answer)