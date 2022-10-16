def solution(number, k):
    answer = []; cnt = k
    for i in range(len(number)):
        answer.append(number[i])
        while ( len(answer) > 1 ) and ( answer[-1] > answer[-2] ) and cnt != 0:
            cnt -= 1
            answer.pop(-2)
        if cnt == 0:
            break
    answer = ''.join(answer) + number[i+1:]
    if len(answer) > len(number)-k: return answer[:k+1]
    return answer