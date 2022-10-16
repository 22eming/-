import "fmt"
func solution(s string, n int) (answer string) {
    for _, i := range s {
        if 'a' <= i && i <= 'z' {
            s := int(i) + n
            if s > 'z' {s -= 26}
            answer += fmt.Sprintf("%c",s)
        } else if 'A' <= i && i <= 'Z' {
            s := int(i) + n
            if s > 'Z' {s -= 26}
            answer += fmt.Sprintf("%c",s)
        } else {
            answer += " "
        }
    }
    return
}