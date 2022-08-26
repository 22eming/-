# time 14m
#2
import re
def solution(skill, skill_trees):
    answer = 0
    p = re.compile(f'[{skill}]')
    for i in skill_trees:
        res = ''.join(p.findall(i))
        if res == []:
            answer += 1
        elif skill == res:
            answer += 1
        elif skill[:len(res)] == res:
            answer += 1

    return answer
    
#1
def solution(skill, skill_trees):
    answer = 0
    for n in skill_trees:
        a,b = [],0
        for i in skill:
            j = n.find(i)
            if j == -1: j = float('inf')
            a.append(j)
        if a == sorted(a): answer += 1
    return answer

def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list = list(skill) 

        for s in  skills: 
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer
    
print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))