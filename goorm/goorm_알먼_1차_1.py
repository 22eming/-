n = int(input())
b_list = list(map(int, input().split()))

answer = 1
for b in b_list:
    answer *= b

print(answer)