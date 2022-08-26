import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[~!@#$%^&*()=+{\}[\]:?,<>/]', "", answer)
    answer = re.sub('\.+' , ".", answer).strip(".")
    if answer == '': answer += "a"
    if len(answer) >= 16: answer = answer[:15].strip(".")
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer


print(solution("=.="))

