n = int(input())
a_list = list(map(int, input().split()))

demical_list = [2]

for i in range(2, n+1):
    for d in demical_list:
        if i%d == 0:
            break
    else:
        demical_list.append(i)

answer = 0
for i in demical_list:
    print(a_list[i-1])
    answer += a_list[i-1]
print(answer)