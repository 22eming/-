import (
	"sort"
	"strings"
)

func solution(s string) string {
	a := strings.Split(s, "")
	sort.Sort(sort.Reverse(sort.StringSlice(a)) )
    return strings.Join(a,"")
}