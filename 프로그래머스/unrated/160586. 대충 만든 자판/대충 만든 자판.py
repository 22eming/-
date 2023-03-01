def solution(keymap, targets):
    answer = []
    dict2key = dict()
    for key in keymap:
        for idx, k in enumerate(list(key)):
            if dict2key.get(k) == None or dict2key[k] > idx:
                dict2key[k] = idx
    
    for target in targets:
        res = 0
        try:
            for t in list(target):
                res += dict2key[t] + 1
            answer.append(res)
        except:
            answer.append(-1)
    
    return answer