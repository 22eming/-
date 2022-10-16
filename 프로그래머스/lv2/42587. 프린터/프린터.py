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