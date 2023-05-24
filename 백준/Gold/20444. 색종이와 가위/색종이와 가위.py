n, k = map(int, input().split())
start, end = 0, n
answer = "NO"
while start <= end:
    mid = (start + end) // 2
    res = (mid + 1) * (n - mid + 1)
    if res == k:
        answer = "YES"
        break
    elif res < k:
        start = mid + 1
    else:
        end = mid - 1
print(answer)