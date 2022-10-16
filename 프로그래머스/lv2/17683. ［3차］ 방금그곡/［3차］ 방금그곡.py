import datetime
def solution(m, musicinfos):
    answer = ['',0]
    mm = []
    for c in m:
        if c == '#':
            mm.append(mm.pop() + c)
        else:
            mm.append(c)
    mt = ''.join(mm)
    musicinfos = [x.split(',') for x in musicinfos]
    for info in musicinfos:
        t1 = datetime.datetime.strptime(info[0], '%H:%M')
        t2 = datetime.datetime.strptime(info[1], '%H:%M')
        dt = ((t2 - t1).seconds)//60
        music = []
        for mu in info[3]:
            if mu == '#':
                music.append(music.pop() + mu)
            else:
                music.append(mu)
        else:
            if dt < len(music):
                music = music[:dt]
            else:
                music = music*(dt//len(music)) + music[:(dt%len(music))]
            for i in range(len(music) - len(mm) + 1):
                if ''.join(music[i:i+len(mm)]) == mt and dt > answer[1]:
                    answer = [info[2], dt]
    if answer[1]:
        return answer[0]
    return '(None)'