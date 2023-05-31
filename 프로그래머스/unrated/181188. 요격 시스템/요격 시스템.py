def solution(targets):
    answer = 0
    end_pos = 0
    targets.sort(key=lambda x: [x[1],x[0]])
    for s, e in targets:
        if s >= end_pos:
            answer += 1
            end_pos = e
    return answer