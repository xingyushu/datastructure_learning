package main  

import "fmt"

func  main(){
	fmt.Println("the start of main func")
	test()
	fmt.Println("the end of main func")
}



func test(){
	defer func(){
		if e :=recover();e!=nil{
			fmt.Printf("panicing %s\n",e)          // panicing bad end 
		}
	}()

	panic("bad end")    //执行到这里 读到错误 则返回 func() recover中  打印出错误  
	fmt.Println("After the bad end")
}


//结果：

// the start of main func
// panicing bad end
// the end of main func
