import "strings"
func solution(n int) string {
    str := strings.Repeat("수박", n/2+1)
    return strings.Join(strings.Split(str, "")[:n], "")
}