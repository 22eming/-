def check(mid,stones, k):
    cnt = 0
    for i in stones:
        if i <= mid:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    start, end = 1, max(stones)
    while start < end - 1:
        mid = (start + end) // 2
        if check(mid,stones,k):
            start = mid
        else:
            end = mid
    return end