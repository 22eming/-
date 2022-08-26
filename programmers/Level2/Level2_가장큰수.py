def solution(numbers):
    answer = ''
    if sum(numbers) == 0: return 0
    
    str_num = list(map(str, numbers))
    sorted_num = sorted(list(map( lambda x: x*3, str_num )), reverse = True)
    answer = ''.join( list( map( lambda x: x[:len(x)//3] , sorted_num)))
    
    return answer

print(solution([3,30,34,5,9]))
