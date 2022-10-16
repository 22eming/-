import "sort"

func solution(array []int, commands [][]int) []int {
	var answer []int
    for _,i := range commands {
        arr := append([]int{}, array[i[0]-1:i[1]]...)
        sort.Ints(arr)
        answer = append(answer, arr[i[2]-1])
	}
    return answer
}