def solution(k, tangerine):
    dict2tan = dict()
    for tanger in tangerine:
        if not dict2tan.get(tanger):
            dict2tan[tanger] = 1
        else:
            dict2tan[tanger] += 1
            
    val = sorted(dict2tan.values(),reverse=True)
    for i, v in enumerate(val):
        k -= v
        if k <= 0:
            return i+1