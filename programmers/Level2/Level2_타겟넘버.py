from itertools import product
def solution(numbers, target):
    plus_minus = [(x, -x) for x in numbers] # +요소 -요소 저장
    s = list(map(sum, product(*plus_minus)))  # 모든 경우의 수의 합
    return s.count(target)

print(solution([1,1,1,1,1],3))