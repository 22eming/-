def solution(word):
    answer = 0
    dic = { "A":"0" ,"E":"1" ,"I":"2" ,"O":"3" ,"U":"4" }
    newword = ''
    for i in word:
        newword += dic[i]

    for i, w in enumerate(newword):
        if i == 0:
            answer += int(w)*781 + 1
        elif i == 1:
            answer += int(w)*156 + 1
        elif i == 2:
            answer += int(w)*31 + 1    
        elif i == 3:
            answer += int(w)*6 + 1 
        elif i == 4:
            answer += int(w) + 1    

    return answer