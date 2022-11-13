def cal(dot_a, dot_b):
    return (dot_a[0] - dot_b[0]) / (dot_a[1] - dot_b[1])

def solution(dots):
    answer = 0
    lin = [cal(dots[i], dots[j]) for i in range(4) for j in range(i+1,4)]
    return int( not len(set(lin)) == len(lin))