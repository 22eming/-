n, k = map(int, input().split())
answer = 0
for _ in range(k):
    y, x = map(int, input().split())
    answer += 1
    if y > 1:
        answer += 1
    if y < n:
        answer += 1
    if x > 1:
        answer += 1
    if x < n:
        answer += 1

print(answer)
