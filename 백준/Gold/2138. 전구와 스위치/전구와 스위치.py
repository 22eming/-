N = int(input())
start = list(map(int, list(input()))) + [0]
end = list(map(int, list(input()))) + [0]


def greed(start, end):
    cnt = 0
    s = start[:]
    for i in range(1, N):
        if s[i - 1] != end[i - 1]:
            cnt += 1
            s[i - 1 : i + 2] = [0 if j else 1 for j in s[i - 1 : i + 2]]
    return cnt if s[:-1] == end[:-1] else float("inf")


res = greed(start, end)
start[0] = 1 - start[0]
start[1] = 1 - start[1]
res = min(res, greed(start, end) + 1)
print(res if res != float("inf") else -1)