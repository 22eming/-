from collections import deque

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