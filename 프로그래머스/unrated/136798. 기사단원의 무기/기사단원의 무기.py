def divisor(number):
    answer = set()
    for n in range(1, int(number**(1/2)+1)):
        if not number%n:
            answer.update([n, number//n])
    return len(answer)
        
def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        p = divisor(n)
        if p > limit:
            answer += power
        else:
            answer += p
        
    return answer