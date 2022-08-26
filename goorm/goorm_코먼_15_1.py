n, k = map(int, input().split())
dic = dict()
for i in range(n):
    time, user = input().split()
    h, m = map(int, time.split(':'))
    now_time = int(h)*60 + int(m)
    
    if user in dic:
        in_out, in_time, total_time = dic.get(user)
        if in_out: # 퇴장
            if in_time <= now_time:
                dic[user] = [0, 0, total_time + now_time-in_time]
            else:
                dic[user] = [0, 0, total_time + now_time + (24*60 - in_time)]
        else:      # 입장
            dic[user] = [1, now_time, total_time]
    
    else:
        dic[user] = [1, now_time, 0]

print(sum([1 for key, v in dic.items() if v[2] >= k*60]))