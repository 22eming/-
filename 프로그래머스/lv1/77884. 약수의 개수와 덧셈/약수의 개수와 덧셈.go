func mea(num int) int {
	answer := 0
    for i:=1; i<=num; i++ {
		if num % i == 0 {
			answer += 1
		}
	}
	return answer
}	

func solution(left int, right int) int {
	result := 0
	for i:=left; i<=right; i++ {
		if mea(i) % 2 == 0 {
			result += i
		} else {
			result -= i
		}
	}
    return result
}