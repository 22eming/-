import (
    "strings"
    "strconv"
)

func solution(s string) int {
	array := [10][2]string{{"zero","0"},{"one","1"},{"two","2"},{"three","3"},{"four","4"},{"five","5"},{"six","6"},{"seven","7"},{"eight","8"},{"nine","9"}}
	for i:=0; i<10; i++ {
        s = strings.Replace(s, array[i][0], array[i][1], -1)
	}
    answer, _ := strconv.Atoi(s)
    return answer
}
// NewReplacer 기억