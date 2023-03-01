from collections import defaultdict
def solution(s):
    answer = []
    words = defaultdict(int)
    for idx, w in enumerate(list(s)):
        if not words[w]:
            answer.append(-1)
            words[w] = idx + 1
        else:
            answer.append(idx + 1 - words[w])
            words[w] = idx + 1 
    return answer
            