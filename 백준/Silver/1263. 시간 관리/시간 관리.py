N = int(input())
todo = [list(map(int, input().split())) for _ in range(N)]
srt_todo = sorted(todo, key=lambda x: [-x[1], x[0]])

ending = float('inf')
for s, t in srt_todo:
    if t < ending:
        ending = t
    ending -= s
    if ending < 0:
        print(-1)
        exit(0)
print(ending)
