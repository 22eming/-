def solution(data, col, row_begin, row_end):
    answer = []
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    data.insert(0, [])
    for i in range(row_begin, row_end+1):
        answer.append(sum([j%i for j in data[i]]))
    
    result = 0
    for ans in answer:
        result ^= ans
    return result