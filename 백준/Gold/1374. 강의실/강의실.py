from sys import stdin
import heapq
N = int(input())
lectures = [list(map(int, stdin.readline().split(" "))) for i in range(N)]
answer = 0
room = []
lectures = sorted(lectures, key=lambda x: x[1])
for lecture in lectures:
    _, start, end = lecture
    while len(room) and room[0] <= start:
        a = heapq.heappop(room)
    heapq.heappush(room, end)
    answer = max(answer, len(room))
print(answer)