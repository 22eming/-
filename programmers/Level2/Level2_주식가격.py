def solution(prices):
    answer = [0]*len(prices)
    for idx, n in enumerate(prices):
        for i in range(idx, len(prices)):
            if prices[i] < n:
                answer[idx] = (i - idx)
                break
        answer[idx] = (i - idx)
    return answer

print(solution([1,2,3,2,3,2,1]),[6, 5, 1, 3, 1, 1, 0])
