def solution(n, times):
    times.sort()
    start = times[0]; end = times[0]*n
    answer = -1
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in times:
            a = mid//i
            if a == 0: break
            cnt += a
        
        if cnt >= n:
            if answer == -1: answer = mid
            else: answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
    return mid



print(solution(6,[1,1,1,1000000]))
