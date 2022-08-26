import collections
def solution(priorities, location):
    answer = 0
    rank = sorted(collections.Counter(priorities).most_common())
    rank = [[x,y] for x,y in rank]
    while True:
        if priorities[0] == rank[-1][0]:
            answer += 1
            if location == 0:
                return answer
                break
            else: location -= 1

            del priorities[0]

            rank[-1][1] -= 1
            if rank[-1][1] == 0: rank.pop()

        else:
            priorities.append(priorities.pop(0))

            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1



# def solution(priorities, location):
#     answer = 0
#     new = []
#     new += priorities
#     n = new[location]
#     a = { n : "a"}
#     res = [n , a[n]]
#     new[location] = res
#     while res in new:  
#         if max(priorities) == priorities[0]:
#             priorities.pop(0)
#             new.pop(0)
#             answer += 1
#         else:
#             priorities.append(priorities.pop(0))
#             new.append(new.pop(0))
#     return answer

# def solution(priorities, location):
#     answer, x = 0, False 
#     while location != -1 or x == False:
#         if max(priorities) == priorities[0]:
#             del priorities[0]
#             location -= 1
#             x = True
#             answer += 1
#         else:
#             priorities.append(priorities[0])
#             del priorities[0]
#             if location == 0:
#                 location = len(priorities)-1
#             else: location -= 1
#             x = False
#     return answer



print(solution([2, 1, 9, 4, 3, 1],1))