def solution(topping):
    def check_topping(topping):
        split_topping = []
        set_topping = set()
        for t in topping:
            if t not in set_topping:
                set_topping.add(t)
                split_topping.append(len(set_topping))
            else:
                split_topping.append(split_topping[-1])
        return split_topping
    
    left = check_topping(topping)[:-1]
    right = check_topping(topping[::-1])[::-1][1:]
    
    cnt = [i==j for i, j in zip(left, right)]
        
    return sum(cnt)
