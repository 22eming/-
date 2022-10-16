def solution(n, lost, reserve):
    for j in [i for i in lost if i in reserve]:
        lost.remove(j)
        reserve.remove(j)
    
    for i in range(1, n+1):  
        if i in lost:
            if (i-1) in reserve:
                reserve.remove(i-1)
                lost.remove(i)
            elif (i+1) in reserve:
                reserve.remove(i+1)
                lost.remove(i)

    return n - len(lost)