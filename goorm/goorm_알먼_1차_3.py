a,b,c,d = map(int, input().split())
answer = 0
answer = max(answer, abs(a-b)+abs(c-d))
answer = max(answer, abs(a-c)+abs(b-d))
answer = max(answer, abs(a-d)+abs(b-c))
print(answer)