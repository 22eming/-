def solution(arr):
    answer = []
    for n in range(len(arr)):
        if n == 0:
            answer.append(arr[n])
        elif arr[n] != arr[n-1]:
            answer.append(arr[n])
    return answer