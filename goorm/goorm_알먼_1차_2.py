n, s = input().split()
answer = 0
for _ in range(int(n)):
    name = input()
    if s in name:
        answer += 1

print(answer)