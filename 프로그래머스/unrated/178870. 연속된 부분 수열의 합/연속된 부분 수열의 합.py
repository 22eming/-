def solution(sequence, k):
    answer = []
    seq, s = [0], 0
    for i in range(len(sequence)):
        s += sequence[i]
        seq.append(s)
       
    start, end, cnt = 0, 1, float("inf")
    while end <= len(sequence):
        if seq[end] - seq[start] == k:
            if end - start < cnt:
                answer = [start, end-1]
                cnt = end - start
            start += 1
                
        elif seq[end] - seq[start] > k:
            if start >= end:
                break
            else:
                start += 1
        else:
            end += 1
    return answer