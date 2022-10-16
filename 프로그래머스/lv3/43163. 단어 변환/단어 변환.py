def solution(begin, target, words):
    answer = 0
    Q = [begin]
    if target not in words: return 0
    while True:
        temp_Q = []
        for word in Q:
            if word == target:
                return answer
            for i in range(len(words)-1,-1,-1):
                word_1 = words[i]
                if sum([x!=y for x,y in zip(word_1,word)]) == 1:
                    temp_Q.append(words.pop(i))
        Q = temp_Q
        answer += 1