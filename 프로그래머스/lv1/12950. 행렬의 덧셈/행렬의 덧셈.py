def solution(arr1, arr2):
    answer = []
    for n in range(len(arr1)):
        answer.extend([[x+y for x,y in zip(arr1[n], arr2[n])]])
    return answer