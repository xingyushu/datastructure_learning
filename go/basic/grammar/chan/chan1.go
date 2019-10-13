package main  

import (
	"fmt"
	"time"
)


func main() {
	ch :=make(chan string)

	go sendData(ch)
	go getData(ch)

	time.Sleep(1e9)
}

func sendData(ch chan string){
	ch <- "Beijing"
	ch <- "Tokyo"
	ch <- "Washington"
	ch <- "London"
	ch <-  "Moscow"
}

func getData(ch chan string){
	var input string 
	for {
		input = <- ch 
		fmt.Printf("%s\n",input)
	}
}