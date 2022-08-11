# 분산처리
#%%
n = int(input())
pow_list = [[10],[1],[2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7, 9, 3, 1], [8,4,2,6], [9,1]]

for _ in range(n):
    a, b = map(int, input().split())
    a %= 10
    print( pow_list[a][(b-1) % len(pow_list[a])])
    