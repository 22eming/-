def solution(babbling):
    answer = 0
    for bab in babbling:
        for i in ["aya", "ye", "woo", "ma" ]:
            bab = bab.replace(i, " ")
        if bab.strip() == "":
            answer += 1
                
    return answer