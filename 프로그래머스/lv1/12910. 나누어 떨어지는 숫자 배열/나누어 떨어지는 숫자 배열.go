import "sort"

func solution(arr []int, divisor int) []int {
	var answer []int

	for _, value := range arr {
		if value%divisor == 0 {
			answer = append(answer, value)
		}
	}

	if len(answer) == 0 {
		return append(answer, -1)
	}

	sort.Ints(answer)
	return answer
}