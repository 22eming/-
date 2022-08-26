def solution(msg):
    answer = []
    book = {}
    for idx,i in enumerate(range(65,91)):
        book[chr(i)] = idx+1
    i = 0
    while i < len(msg):
        j = 2
        while msg[i:i+j] in book.keys() and i+j <= len(msg):
            j += 1
        else:
            answer.append(book[msg[i:i+j-1]])
            book[msg[i:i+j]] = len(book.values())+1
            if j > 2:
                i += j-2
        i += 1
    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))
