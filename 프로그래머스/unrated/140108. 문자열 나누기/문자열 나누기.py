def solution(s):
    answer = cnt = 0
    pass_word = True
    for idx,word in enumerate(list(s)):
        if pass_word:
            answer += 1
            start = word
            pass_word = False
        elif start != word:
            if not cnt:
                pass_word = True
            else:
                cnt -= 1
        else:
            cnt += 1
    
    return answer