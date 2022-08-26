from collections import deque

def solution(queue1, queue2):
    q1, q2, cnt = deque(queue1), deque(queue2), 0
    max_len = len(q1) + len(q2)
    while cnt < max_len:
        sq1, sq2 = sum(q1), sum(q2)
        if sq1 == sq2:
            return cnt
        elif sq1 > sq2:
            q2.append(q1.popleft())
        else:
            q1.append(q2.popleft())
        cnt += 1
    return -1

def solution(queue1, queue2):
    f, b = 0, 0
    sum_f, sum_b, len_q = sum(queue1), sum(queue2), len(queue1)+len(queue2)
    queue1, queue2 = queue1+queue2, queue2+queue1
    while 1:
        if sum_f == sum_b:
            return f+b
        elif sum_f > sum_b:
            sum_f -= queue1[f]
            sum_b += queue1[f]
            f += 1
        else:
            sum_f += queue2[b]
            sum_b -= queue2[b]
            b += 1
        if f == len_q or b == len_q:
            return -1
    
q1, q2 = [1,2,1,2], [1,10,1,2]
print(solution(q1, q2))