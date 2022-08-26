num = [3, 30, 34, 5, 9]
# [3, 30, 34, 5, 9]  [0, 0, 0, 0, 0] [0, 5, 10, 15, 20] [1000, 0, 5, 99, 100] 
# print(num[0])

def solution(numbers):
    answer = ''
    if max(numbers) == 0:
        return "0"
    str_num = list(map(str, numbers))
    print(str_num)
    a = sorted(list(map(lambda x : x*3 ,str_num)) , reverse=True)
    answer = "".join(list(map(lambda x : x[:len(x)//3], a)))
    return answer

print(solution(num))
continue