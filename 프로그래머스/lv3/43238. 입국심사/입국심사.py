def solution(n, times):
    times.sort()
    res = cacul(times[0], times[0]*n, times, n)
    return res

def cacul(start, end, times, n):
    answer = float("inf")
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for i in times:
            tmp = mid // i
            if tmp == 0: break
            cnt += tmp
        
        if cnt >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
    return answer