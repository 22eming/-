import (
    "strconv"
	"sort"
    "strings"
)

func solution(numbers []int) string {
    number := []string {}
    max := 0
    for i:=0; i<len(numbers); i++ {
        if max < numbers[i] { max = numbers[i]}
        number = append(number, strconv.Itoa(numbers[i]))
    }

    if max == 0 {
        return "0"
    }

    sort.Slice(number, func(i, j int) bool {
        s1 := strings.Repeat(number[i], 3)
        s2 := strings.Repeat(number[j], 3)
        return s1 > s2
    })
    answer := strings.Join(number, "")
    return answer
}