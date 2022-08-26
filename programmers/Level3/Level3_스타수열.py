from collections import Counter


def solution(a):
    answer = 0
    common = Counter(a).most_common()
    for c in common:
        if c[1] <= answer:
            break
        cnt = 0
        check = [0]*len(a)
        for i in range(len(a)):
            if a[i] == c[0]:
                check[i] = 1
                if i == len(a)-1:
                    if check[i-1] == 0:
                        cnt += 1
                else:
                    if a[i+1] == c[0]:
                        check[i+1] = 1
                    if i > 0:
                        if check[i-1] == 0:
                            check[i-1] = 1
                            cnt += 1
                        elif check[i+1] == 0:
                            check[i+1] = 1
                            cnt += 1
                    else:
                        if check[i+1] == 0:
                            check[i+1] = 1
                            cnt += 1
        answer = max(answer, cnt)
    return answer*2


answer = [5, 2, 3, 3, 5, 3]
print(solution(answer))
