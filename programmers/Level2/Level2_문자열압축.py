def solution(s):
    answer = len(s)
    result = ''
    for cut in range(1, len(s)//2 + 1):
        cnt = 1
        temp = s[:cut]
        for x in range(cut, len(s), cut):
            if s[x:x+cut] == temp:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + temp
                temp = s[x:x+cut]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + temp
        answer = min(answer, len(result))
        result = ''
    return answer

print(solution("abcabcabcabcdededededede"))
