from sys import stdin

N = int(stdin.readline())
grade = [0,0,0,0,0]
answer = [0, 0]
for i in range(N):
    a, b = map(int, stdin.readline().split())
    a, b = a-1, b-1
    for i in range(5):
        if i != a and i != b:
            grade[i] = 0
    
    grade[a] += 1
    if a != b:
        grade[b] += 1
    
    if grade[a] > answer[0] or ( grade[a] == answer[0] and a < answer[1]):
        answer = [grade[a], a+1]
    if grade[b] > answer[0] or ( grade[b] == answer[0] and b < answer[1]):
        answer = [grade[b], b+1]

print(' '.join(map(str, answer)))