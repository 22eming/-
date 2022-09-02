line_len = lambda x, y, cx, cy : ((cx-x)**2 + (cy - y)**2) ** 0.5

T = int(input())
answer = []
for _ in range(T):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    circle = [list(map(int, input().split())) for _ in range(n) ]
    # 시작점이 원 안에 있거나 도착점이 원 안에 있는 경우
    for cx, cy, r in circle:
        l1, l2 = line_len(x1,y1,cx,cy), line_len(x2,y2,cx,cy)
        if l1 <= r and l2 > r:
            result += 1
        if l2 <= r and l1 > r:
            result += 1
    answer.append(result)
    
print('\n'.join(map(str, answer)))