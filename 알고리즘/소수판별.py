import math

def is_prime_number(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return num


# import math


# def is_prime_number(x):
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# print(is_prime_number(26))


print(solution(26))
