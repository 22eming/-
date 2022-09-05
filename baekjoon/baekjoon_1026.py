N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
A, B = sorted(A), sorted(B, reverse=True)

answer = 0
for i in range(N):
    answer += A[i] * B[i]
print(answer)
