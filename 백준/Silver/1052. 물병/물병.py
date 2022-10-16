N, K = map(int, input().split())

cnt = 0
while bin(N).count('1') > K:
    idx = bin(N).rfind('1')
    temp = int('0b'+bin(N)[idx:], 2)
    N += temp
    cnt += temp
print(cnt)