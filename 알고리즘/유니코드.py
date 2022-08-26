def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif ord(i) < 123 and ord(i)+n > 122:
            answer += chr(ord(i) + n - 26)
        elif ord(i) < 91 and ord(i)+n > 90:
            answer += chr(ord(i) + n - 26)
        else:
            answer += chr(ord(i)+n)
    return answer

print(solution("a B z", 4))

# print(type(ord("a")))