from random import*
total = 0

for sonim in range(1, 51):
    time = int(random()*50+1)
    if 5 <= time <= 15:
       total += 1
    print("{0}번째 손님 (소요시간 : {1}분)".format(sonim, time))

print("총 탑승 승객 : {0}분".format(total))
