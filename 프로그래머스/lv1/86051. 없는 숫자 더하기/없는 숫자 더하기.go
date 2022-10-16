func solution(numbers []int) int {
	num := 0
	for i := 0; i < len(numbers); i++ {
		num += numbers[i]
	}
	return 45 - num
}