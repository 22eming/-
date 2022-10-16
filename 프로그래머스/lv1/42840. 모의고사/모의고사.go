func solution(answers []int) (result []int ){
	answer := []int {0,0,0}
	candi := [][]int {
		{1,2,3,4,5},
		{2, 1, 2, 3, 2, 4, 2, 5},
		{3, 3, 1, 1, 2, 2, 4, 4, 5, 5},
	}
	for i:=0; i<len(answers); i++ {
		for j:=0; j<3; j++ {
			if answers[i] == candi[j][i%len(candi[j])] {
				answer[j] += 1
			}
		}
	}
	max := -1
	for i:=0; i<3; i++ {
		if answer[i] > max {
			result = []int {i+1}
			max = answer[i]
		} else if answer[i] == max {
			result = append(result, i+1)
		}
	}
	return
}