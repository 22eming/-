def solution(name):
    answer = 0
    res_min = len(name.rstrip("A"))
    for n in name:
        if n == "A": pass
        elif ord(n) < 78:
            answer += ord(n)-65
        else:
            answer += 91 - ord(n)

    for i in range(-(len(name)//2), (len(name)//2)+1):
        if i < 0:
            res_min = min(res_min, len(name[i:][::-1]+name[i+1:]+name[:i].rstrip("A")))
        elif i > 0:
            res_min = min(res_min, len(name[1:i]+name[:i-1][::-1]+name[i:][::-1].rstrip("A")))
    return answer + res_min


def solution(name):
    answer = [ord(i) - 65 if ord(i) < 78 else 91 - ord(i) for i in name ]
    ans = []
    for i in range(len(answer)//2+1):
        res = answer[i:]
        result = (i-1)*2
        if result < 0: result = 0
        if sum(res) != 0:
            for j in range(-len(answer)+i,0):
                res.pop(-1)
                result += 1
                if sum(res) == 0:
                    ans.append(sum(answer) + result)
                    break
        else:
            return sum(answer) + result
    return min(ans)

    
print(solution("JAN"))

# a c d e f g h i j k l m n o p q r s t u v w x y z
