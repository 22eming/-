answers = [1,2,3,4,5]
def solution(answers):
    answer = []
    one, two, tre,a,b,c= [1,2,3,4,5]*((len(answers)//5)+1), [2,1,2,3,2,4,2,5]*((len(answers)//8)+1), [3,3,1,1,2,2,4,4,5,5]*((len(answers)//10)+1),0,0,0
    for n in range(len(answers)): 
        if one[n] == answers[n]: a += 1
        if two[n] == answers[n]: b += 1
        if tre[n] == answers[n]: c += 1
    x = max(a,b,c)
    if a==x: answer.append(1)
    if b==x: answer.append(2)   
    if c==x: answer.append(3)
    sorted(answer)
    return answer

# def solution(answers):
#     p = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     s = [0] * len(p)

#     for q, a in enumerate(answers):
#         for i, v in enumerate(p):
#             if a == v[q % len(v)]:
#                 s[i] += 1
#     return [i + 1 for i, v in enumerate(s) if v == max(s)]