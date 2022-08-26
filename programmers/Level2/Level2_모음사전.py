def solution(word):
    answer = 0
    dic = { "A":"0" ,"E":"1" ,"I":"2" ,"O":"3" ,"U":"4" }
    a = [781,156,31,6,1]
    newword = ''
    for i in word:
        newword += dic[i]

    for i, w in enumerate(newword):
        answer += int(w)*a[i] + 1

    return answer

print(solution("I"))