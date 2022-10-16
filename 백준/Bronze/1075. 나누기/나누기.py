N, F  = input(), int(input())

N = int(N[:-2]+"00")
if N % F == 0:
    print("00")
else:
    print(str(F-(N % F)).rjust(2,"0"))