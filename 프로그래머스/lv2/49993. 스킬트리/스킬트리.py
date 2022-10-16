def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees: #"CB"
        skill_list = list(skill) #"C" "B" "D" "k"

        for s in  skills:  #"C"
            if s in skill: #"C" in "C""B""D""K"
                if s != skill_list.pop(0): #"C" = "C"
                    break
        else:
            answer += 1
    return answer