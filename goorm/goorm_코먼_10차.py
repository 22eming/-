import sys
from itertools import combinations

def solution(data):
    vilis = [ set(map(int, s[2:].split())) for s in data.split("\n")][:-1]

    jupas = set()
    for v in vilis:
        jupas |= v
        
    a = set()
    for i in range(len(vilis)-1):
        for j in range(i+1, len(vilis)):
            a.update(vilis[i] & vilis[j])

    for i in range(1, len(a)):
        for com_a in combinations(a, i):
            com_a = set(com_a)
            if [v for v in vilis if v & com_a == set()] == []:
                print(i)
                break
        else:
            continue
        break

data = "3 9 3 5\n4 3 8 2 9\n5 6 4 7 1 3\n5 3 9 1 7 5\n"
data1 = "3 6 4 9\n4 1 5 2 14\n3 9 10 4\n4 13 10 1 3\n3 13 10 7\n"
solution(data)