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