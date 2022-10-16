func solution(a int, b int) string {
	month := []int {0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335}
	day := []string {"THU","FRI","SAT","SUN","MON","TUE","WED"}

    return day[ (month[a-1] + b) % 7 ]
}