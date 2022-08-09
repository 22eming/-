#%% 
# 1271

n, m = map(int, input().split())

print(n // m)
print(n % m)

#%% 
# 2338

a, b = int(input()), int(input())
print(f"{a+b}\n{a-b}\n{a*b}")

#%% 
# 2558

a, b = int(input()), int(input())
print(a+b)

#%% 
# 3003
answer, right_chess = "", [1,1,2,2,2,8]
dong = list(map(int, input().split()))
for i, j in zip(right_chess, dong):
    answer += str(i - j) + " "
print(answer[:-1])

#%%
# 4101
while 1:
    a, b = map(int, input().split())
    if a + b == 0: break
    print("Yes") if a > b else print("No")

#%%
# 4999
print("no") if len(input()) < len(input()) else print("go")

#%%
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 정수 a와 b가 주어진다. (1 ≤ a < 100, 1 ≤ b < 1,000,000)

# 출력
# 각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 출력한다.

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(str(a**b)[-1:])

# %%
