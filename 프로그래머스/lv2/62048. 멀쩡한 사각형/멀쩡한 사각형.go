func gcd(a int, b int) int {
	if a==0 { return b}
	return gcd(b%a, a)
}

func solution(w int, h int) int64 {
	return int64(w*h -w -h + gcd(w,h))
}