func solution(absolutes []int, signs []bool) int {
	answer := 0
    for idx, sign := range signs {
		if sign {
			answer += absolutes[idx]
        } else {
            answer -= absolutes[idx]
        }
	}
    return answer
}