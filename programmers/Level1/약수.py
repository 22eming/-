def div(num):
    if num == 1: return -1
    result = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            result.append(i)
            result.append(int(num/i))

    result = list(set(result))
    if len(result) % 2 == 0:
        return num
    else:
        return -num


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += div(i)
    return answer

print(solution(1,2))