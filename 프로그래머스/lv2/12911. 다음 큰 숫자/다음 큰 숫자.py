def solution(n):
    s = bin(n)[3:]
    # if s.count("1") in [0,len(s)]: res = "10" + s
    if s.lstrip("1").count("1") > 0 :
        a = s.rfind("1")
        b = s[:a].rfind("0")
        res = "1" + s[:b] + "1" + ''.join(["0"]*(s[b:].count("0")) + ["1"]*(s[b:].count("1")-1))
    else: res = "10" + ''.join(["0" for n in range(s.count("0"))]) + ''.join(["1" for i in range(s.count("1"))])
    return int("0b"+ res, 2)