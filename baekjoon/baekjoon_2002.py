N = int(input())
input_car = {input(): i for i in range(N)}
visited = [False]*N
answer = 0

for _ in range(N):
    out_car = input()
    i = input_car[out_car]
    sum_i = sum(visited[:i])
    if sum_i < i:
        answer += 1
    visited[i] = True
print(answer)