def solution(s):
    cnt = 0
    for n in range(len(s)):
        if s[n] == "(": cnt += 1
        elif s[n] == ")": cnt -= 1
        if cnt < 0: return False
    return cnt == 0