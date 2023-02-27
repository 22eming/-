from itertools import product

def check(discounts, users, emoticons):
    total_peo, total_cost = 0, 0
    for want_dis, cost in users:
        tmp_cost = 0
        for idx, discount in enumerate(discounts):
            if want_dis <= discount:
                tmp_cost += emoticons[idx]*(1-discount*0.01)
        if tmp_cost >= cost:
            total_peo += 1
        else:
            total_cost += tmp_cost
    return total_peo, total_cost
                

def solution(users, emoticons):
    answer = []
    max_peo, max_cost = 0, 0
    for discounts in list(product([10,20,30,40],  repeat=len(emoticons))):
        tmp_peo, tmp_cost = check(discounts, users, emoticons)
        if max_peo < tmp_peo:
            max_peo = tmp_peo
            max_cost = tmp_cost
        elif max_peo == tmp_peo and max_cost < tmp_cost:
            max_cost = tmp_cost
            
    return [max_peo, int(max_cost)]