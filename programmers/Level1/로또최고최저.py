def solution(lottos, win_nums):
    win_num = [ i in win_nums for i in lottos ]
    max_num = sum(win_num) + lottos.count(0)
    min_num = sum(win_num)
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    return [dic[max_num], dic[min_num]]

print(solution([44, 1, 0, 0, 31, 25]	,[31, 10, 45, 1, 6, 19]))