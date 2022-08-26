def solution(price, money, count):
    totalcount=0
    for i in range(1,count+1):
        totalcount += i
    result = price*totalcount
    
    if money >= result:
        return 0
    else:
        return result - money
