import (
	"fmt"
	"strings"
)

func solution(phone_number string) string {
    answer := strings.Repeat("*", len(phone_number)-4)
    for _, i := range phone_number[len(phone_number)-4:]{
        answer += fmt.Sprintf("%c", i)
    }
    return answer
}