y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
        
import datetime as dt
d_day = str(dt.date(y2, m2, d2) - dt.date(y1, m1, d1)).split()[0]

gg = False
if y2-y1 > 1000:
    gg = True
elif y2-y1 == 1000:
    if m2 > m1:
        gg = True
    elif m2 == m1:
        if d2 >= d1:
            gg = True
            
if not gg:
    print(f'D-{d_day}')
else:
    print('gg')
