import numpy as np
def solution(scores):
    answer = ''
    scores = np.transpose(scores)
    
    for j,i in enumerate(scores):
        i = list(i)
        if (i[j] == max(i) and i.count(i[j]) == 1) or (i[j] == min(i) and i.count(i[j]) == 1) :
            m = ( sum(i) - i[j] ) / (len(i)-1)
        else:
            m = np.mean(i)
        
        if m >= 90:
            answer += 'A'
        elif m >= 80:
            answer += 'B'
        elif m >= 70:
            answer += 'C'
        elif m >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])