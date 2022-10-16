def solution(operations):
    res = []
    for n in operations:
        if n[0] == "I":
            res.append(int(n[2:]))
        elif len(res) > 0:
            if n[2] == "1":
                del res[res.index(max(res))]
            else:
                del res[res.index(min(res))]
    if res == []: return [0,0]
    return [max(res), min(res)]