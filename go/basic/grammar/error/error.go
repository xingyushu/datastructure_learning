package main   

import (
	"errors"
	"fmt"
)



var errNotFound error  = errors.New("Error Not Found") 

func main(){
	fmt.Printf("error:%v\n",errNotFound)
	if _,err :=Sqrt(-4);err!=nil{
		fmt.Printf("Err is:%s\n",err)
	}
	panic("error occur")
}


func  Sqrt(f float64) (float64,error){
	if f<0{
		return 0,errors.New("the parameter is negative")
	}
	return  f,nil
}