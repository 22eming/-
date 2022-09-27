N, K = map(int, input().split())
people = list(range(1, N+1))

answer = []
num = 0

for _ in range(N):
    num += K-1
    if num >= len(people):
        num = num % len(people)
    answer.append(people.pop(num))

print("<", ', '.join(map(str, answer)), ">", sep='')
