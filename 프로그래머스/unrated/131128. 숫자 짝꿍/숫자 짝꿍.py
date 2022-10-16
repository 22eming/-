from collections import Counter

def solution(X, Y):
    answer = ''
    result = [0]*10
    x_count = Counter(X)
    y_count = Counter(Y)
    for key, val in x_count.items():
        if y_count.get(key):
            result[int(key)] = min(val, y_count[key])
    
    if not sum(result):
        return "-1"
    elif not sum(result[1:]):
        return "0"

    for i in range(9, -1, -1):
        answer += f'{i}'*result[i]
    return answer