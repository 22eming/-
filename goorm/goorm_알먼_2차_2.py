N = int(input())
s = input()

last_s = s[0]
answer = 1

for i in range(1, len(s)):
    if last_s != s[i]:
        last_s = s[i]
        answer += 1

answer += 1

print(answer)
