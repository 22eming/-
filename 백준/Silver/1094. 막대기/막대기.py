x = int(input())
stick, cnt, sum_s = [64, 32, 16, 8, 4, 2, 1], 0, 0

for s in stick:
    if sum_s + s <= x:
        sum_s += s
        cnt += 1
        if sum_s == x:
            break
print(cnt)