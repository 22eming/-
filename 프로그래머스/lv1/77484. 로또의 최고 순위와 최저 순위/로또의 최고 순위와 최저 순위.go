func solution(lottos []int, win_nums []int) []int {
	zero := 0
	correct := 0
	
	for _, i := range lottos {
		if i == 0 {	zero += 1}
		for _, j := range win_nums {
			if i == j {	correct += 1}
		}
	}
	max := 7 - (zero + correct)
	min := 7 - correct
	if max > 6 { max = 6}
	if min > 6 { min = 6}
	answer := []int {max, min}

    return answer
}