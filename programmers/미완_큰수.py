def solution(number, k):
    answer,mx,l, m = '', 0, k, len(number)
    if list(set(number)) == ['9']: return number[k:]
    while  mx < k:
        num = number[:l+1].index(max(number[:l+1]))
        answer += number[num]
        number = number[num+1:]
        mx += num
        l -= num
        if len(answer) == (m-k):
            return answer
    return (answer + number)

print(solution("999999",3))