def solution(nums):
    a = list(set(nums))
    if len(nums)/2 >= len(a):
        return len(a)
    else:
        return int(len(nums)/2)