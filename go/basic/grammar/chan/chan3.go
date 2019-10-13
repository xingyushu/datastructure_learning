package  main  

import (
    "fmt"
    "time"
)

func  main(){
    fmt.Println("the start of main")
    go longWait()
    go shortWait()
    fmt.Println("the sleep of main")
    time.Sleep(10*1e9)
    fmt.Println("the end of main")
}


func longWait(){
    fmt.Println("the start of longWait")
    time.Sleep(5*1e9)
    fmt.Println("the end of longWait")
}



func shortWait(){
    fmt.Println("the start of shortWait")
    time.Sleep(2*1e9)
    fmt.Println("the end of shortWait")
}


// result :
// the start of main  
// the sleep of main
// the start of longWait
// the start of shortWait
// the end of shortWait
// the end of longWait
// the end of main