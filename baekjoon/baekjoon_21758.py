N = int(input())
honey = list(map(int, input().split()))

honey_plus = honey.copy()
for i in range(1, N):
    honey_plus[i] += honey_plus[i-1]

print("꿀 누적 합 : ", honey_plus)
result = 0
for i in range(1, N-1):
    # 왼쪽 2마리 -> 한마리는 가장 왼쪽 고정 어차피 앞으로 가봤자 못 먹는 꿀만 많아짐.
    # 꿀은 오른쪽 끝 고정
    result = max(result, honey_plus[-1]*2 -
                 honey[0] - honey[i] - honey_plus[i])

    # 오른쪽 2마리 -> 한마리 가장 오른쪽 고정
    # 꿀은 가장 왼쪽 고정
    result = max(result, honey_plus[-1]-honey[-1]-honey[i] + honey_plus[i-1])

    # 오1 왼 1 -> 꿀통 움직임
    result = max(result, honey_plus[i]-honey[0] +
                 honey_plus[-1]-honey_plus[i-1]-honey[-1])
print(result)
