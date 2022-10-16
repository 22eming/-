def solution(sizes):
    big, small = 0, 0
    for i in sizes:
        i.sort()
        if i[0] > small:
            small = i[0]
        if i[1] > big:
            big = i[1]
    return big*small