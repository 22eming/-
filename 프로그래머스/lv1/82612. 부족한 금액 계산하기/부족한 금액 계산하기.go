func solution(price int, money int, count int) int64 {
	need := price * count * (count+1) / 2
	answer := int64(need) - int64(money)
	if answer < 0 { return 0}
    return answer
}