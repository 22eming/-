test_n = int(input())

for i in range(test_n):
    west, east = map(int, input().split())
    result = 1
    for j in range(1,west+1):
        result *= east / j
        east -= 1    
    print(round(result))
