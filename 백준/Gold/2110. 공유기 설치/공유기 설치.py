N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])


def binary(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        current = house[0]
        cnt = 1

        for i in range(1, len(house)):
            if house[i] >= current + mid:
                current = house[i]
                cnt += 1

        if cnt >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


print(binary(1, house[-1] - house[0]))
