import heapq

def solution(jobs):
    jobs.sort()
    answer, time = 0, 0
    len_jobs = len(jobs)

    while jobs:
        if time >= jobs[0][0]:
            line_time = sorted(list(filter(lambda x: x if x[0] <= time else False , jobs)), key = lambda x: x[1])
            res = heapq.heappop(line_time)
            time += res[1]
            answer += time - res[0]
            jobs = line_time + jobs[len(line_time)+1:] 
        else:
            time = jobs[0][0] 
    return int(answer/len_jobs)

# print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[100, 100], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)