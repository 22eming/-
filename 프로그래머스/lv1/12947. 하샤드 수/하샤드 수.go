func solution(x int) bool {
    n := x
    sum := 0
    for n != 0 {
        sum += n%10
        n /= 10
    }
    sum += n
    println(sum)
    if x % sum == 0 {
        return true
    } else {
        return false
    }
}