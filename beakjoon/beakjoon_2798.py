# N = list(map(int, input().split()))
# M = list(map(int, input().split()))
N = [10, 500]
M = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
M.sort()
res = []
for i in range(N[0]-2):
    for j in range(i+1,N[0]-1):
        for k in range(i+2,N[0]):
            if M[i] + M[j] + M[k] <= N[1]:
                res.append(M[i] + M[j] + M[k])
            else:
                break

print(max(res))


# print(solution([10, 500],[93, 181, 245, 214, 315, 36, 185, 138, 216, 295]))