from collections import defaultdict, deque


def solution(arr, processes):
    answer = []
    wait_que = deque()
    work = []
    dic = defaultdict(list)

    for pro in processes:
        p = pro.split()
        dic[int(p[1])].append(p)
    
    t = min(dic.values())
    while work or wait_que:
        if dic[t]:
            wait_que.append(dic[t])
        if work == []:
            wait_que.popleft()
        if work[]
    return answer

# 읽기 -> 새로운 읽기 가능
# 쓰기 -> 새로운 읽기 쓰기 대기
# 읽기 -> 새로운 쓰기 대기
# 쓰기 -> 새로운 읽기 대기
# 쓰기 > 읽기
# 먼저 요청된 쓰기


print(solution(["1", "2", "4", "3", "3", "4", "1", "5"],	["read 1 3 1 2",
      "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]))
