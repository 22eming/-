L, R = input().split()
answer = 0

if len(L) != len(R):
    print(answer)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                answer += 1
        else:
            break
    print(answer)
