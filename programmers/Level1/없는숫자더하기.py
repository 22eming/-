def solution(numbers):
    res = [1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        res.remove(i)
    return sum(res)

print(solution([1,2,3,4,6,7,8,0]))