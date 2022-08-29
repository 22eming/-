num = int(input())
N = []
for i in range(num):
    N.append(list(map(int, input().split())))

for i in N:
    aver = sum(i[1:])/i[0]
    cnt = 0
    for j in i[1:]:
        if j > aver: cnt += 1
    rate = cnt/i[0] * 100
    print(f'{rate:.3f}%')