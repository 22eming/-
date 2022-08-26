def solution(goods):
    answer = [[] for i in range(len(goods))]

    for i in range(len(goods)):
        word_len_true = False
        # 단어 길이
        for j in range(1, len(goods[i])):
            for k in range(len(goods[i])-j+1):

                word = goods[i][k:k+j]
                true_serch = True
                for l in range(len(goods)):
                    if i == l:
                        continue
                    if word in goods[l]:
                        true_serch = False
                if true_serch:
                    if word not in answer[i]:
                        answer[i].append(word)
                    word_len_true = True
            if word_len_true:
                break

    for i in range(len(answer)):
        answer[i] = " ".join(s for s in sorted(answer[i]))
        if answer[i] == "":
            answer[i] = "None"
    return answer

# 1개 문자열 ...


print(solution(["pencil", "cilicon", "contrabase", "picturelist"]))
