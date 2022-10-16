n = int(input())
answer = 0
for _ in range(n):
    group_word = list(input())
    visited = set()
    temp = ''
    for g_w in group_word:
        if g_w in visited and g_w != temp:
            break
        visited.add(g_w)
        temp = g_w
    else:
        answer += 1

print(answer)