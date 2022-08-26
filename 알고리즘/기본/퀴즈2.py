from random import*

lst = range(1, 21)
lst = list(lst)
shuffle(lst)

winner = sample(lst, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("-- 축하합니다 --")
