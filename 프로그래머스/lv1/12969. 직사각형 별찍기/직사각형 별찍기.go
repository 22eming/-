package main

import (
	"fmt"
	"strings"
)
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    for i:=0; i<b; i++ {
        fmt.Println(strings.Repeat("*",a))
    }
}