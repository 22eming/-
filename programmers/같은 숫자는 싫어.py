s = [1,1,3,3,0,1,1]
def solution(arr):
    answer = list(set(arr))
    return answer

# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a



print(solution(s))