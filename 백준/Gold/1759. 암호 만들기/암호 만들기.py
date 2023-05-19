def back_t(count, index):
    if count == L:
        v, c = 0, 0

        for i in range(L):
            if answer[i] in mother:
                c += 1
            else:
                v += 1

        if v >= 2 and c >= 1:
            print("".join(answer))

        return

    for i in range(index, C):
        answer.append(alpha[i])
        back_t(count + 1, i + 1)
        answer.pop()


L, C = map(int, input().split())
alpha = sorted(input().split())
mother = ("a", "e", "i", "o", "u")
answer = []
back_t(0, 0)