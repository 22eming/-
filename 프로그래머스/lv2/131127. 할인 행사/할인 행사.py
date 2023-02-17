from collections import deque
def solution(want, number, discount):
    answer = 0
    dict_of_want = {w:i for i, w in enumerate(want)}
    que = deque([])
    i = 0
    while i != len(discount):
        d = discount[i]
        que.append(d)
        if d in dict_of_want:
            number[dict_of_want[d]] -= 1
        if i >= 9:
            if not any(number):
                answer += 1
            d_out = que.popleft()
            if d_out in dict_of_want:
                number[dict_of_want[d_out]] += 1
        i += 1
        
    return answer