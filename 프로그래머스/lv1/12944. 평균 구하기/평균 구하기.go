func solution(arr []int) float64 {
	answer := 0
	for _,i := range arr {
		answer += i
	}
	return float64(answer)/float64(len(arr))
}