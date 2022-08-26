def solution(numbers):
    answer = []
    for n in range(len(numbers)-1):
        x, y = len(numbers), n+1
        while y != x:
            answer.append(numbers[n] + numbers [y])
            y += 1
    return sorted(list(set(answer)))

solution([2,1,3,4,1])