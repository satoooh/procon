package main
import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

var sc = bufio.NewReaderSize(os.Stdin, 1024*1024*10)

func main() {
    N := getStdinInt()
    s := make([]int, N)
    sum := 0
    for i := 0; i < N; i++ {
        s[i] = getStdinInt()
        sum += s[i]
    }

    var ans int
    if sum%10 != 0 {
        ans = sum
    } else {
        // s の 10 の倍数で無い最小値を見つける
        minS := sum // すべて 10 の倍数なら ans = 0 となるよう初期値を sum でおく
        for i := 0; i < N; i++ {
            if s[i]%10 != 0 && s[i] < minS {
                minS = s[i]
            }
        }
        ans = sum - minS
    }

    fmt.Println(ans)
}


func getStdin() string {
    return readLine()
}
func getStdinInt() int {
    str := getStdin()
    res, _ := strconv.Atoi(str)
    return res
}
func getStdinIntArr() []int {
    str := getStdin()
    list := strings.Split(str, " ")
    res := make([]int, len(list))
    for idx, v := range list {
        res[idx], _ = strconv.Atoi(v)
    }
    return res
}
func getStdinArr() []string {
    str := getStdin()
    list := strings.Split(str, " ")
    return list
}
func getStdinIntArr64() []int64 {
    str := getStdin()
    list := strings.Split(str, " ")
    res := make([]int64, len(list))
    for idx, v := range list {
        res[idx], _ = strconv.ParseInt(v, 10, 64)
    }
    return res
}
func readLine() string {
    buf := make([]byte, 0, 0)
    for {
        l, p, e := sc.ReadLine()
        if e != nil {
            panic(e)
        }
        buf = append(buf, l...)
        if !p {
            break
        }
    }
    return string(buf)
}