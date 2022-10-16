import "fmt"

func solution(seoul []string) string {
    for idx, i := range seoul {
		if i == "Kim" {
			return fmt.Sprintf("김서방은 %d에 있다", idx)
		}
	}
    return ""
}