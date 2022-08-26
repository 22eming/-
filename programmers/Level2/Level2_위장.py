def solution(clothes):
    answer = 1
    dic = {}

    for val, key in clothes:
        if dic.get(key) == None:
            dic[key] = [val]
        else:
            dic[key].append(val)

    for key in dic:
        answer *= len(dic[key]) + 1 # 선택 하지않거나 한개씩 선택했을때

    return answer - 1 #모두 선택하지 않았을때 제외

print(solution( [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]] ))