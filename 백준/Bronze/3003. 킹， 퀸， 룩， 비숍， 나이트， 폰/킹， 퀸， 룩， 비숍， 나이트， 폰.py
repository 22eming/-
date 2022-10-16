answer, right_chess = "", [1,1,2,2,2,8]
dong = list(map(int, input().split()))
for i, j in zip(right_chess, dong):
    answer += str(i - j) + " "
print(answer[:-1])