board = input()
answer, cnt = '', 0
for b in board:
    if b == 'X':
        cnt += 1
        if cnt == 4:
            answer += 'AAAA'
            cnt = 0
    elif b == '.':
        if cnt == 2:
            answer += 'BB'
            cnt = 0
        elif cnt != 0:
            print(-1)
            break
        answer += '.'
else:
    if cnt == 2 or cnt == 0:
        print(answer + 'B'*cnt)
    elif cnt != 0:
        print(-1)
