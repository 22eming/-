# from itertools import combinations
# def solution(numbers, target):
#     answer = 0
#     res = (sum(numbers) - target)//2
#     for n in range(1, len(numbers)):
#         a = list(combinations(numbers, n))
#         b = list(map(sum, a))
#         print(b)
#         if min(b) > res: break
#         answer += b.count(res)
#     return answer

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


print(solution([1,1,1,1,1],3))