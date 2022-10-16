def length(location,i):
    res =  abs(i - location)
    if res == 0: return 0
    elif res in [1,3]: return 1
    elif res in [2,4,6]: return 2
    elif res in [5,7,9]: return 3
    elif res in [8,10]: return 4
    else: return 5

def solution(numbers, hand):
    answer = ''
    L_location = 10; R_location = 12
    for idx,i in enumerate(numbers):
        if i == 0: numbers[idx] = 11
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            L_location = i
        elif i in [3,6,9]:
            answer += "R"
            R_location = i
        else:
            if length(L_location,i) == length(R_location,i):
                if hand == "right":
                    R_location = i
                    answer += "R"
                else:
                    L_location = i
                    answer += "L"
            elif length(L_location,i) > length(R_location,i):
                answer += "R"
                R_location = i
            else:
                answer += "L"
                L_location = i

    return answer