package main  

import "fmt"

type  Book struct{
	Title string  
	Nums  int 
}


type Person struct{
	Name string 
	Age int  
	Address  string  
}

type Interval struct{
	Start int 
	End int 
}

func changeBook(book Book) string{
	book.Title = "book1"
	return book.Title 

}

func changeBook2(book *Book){
	book.Title = "book1"
	// return book.Title 

}


func main(){
	var book1 Book
	book1.Title = "Hello world"
	book1.Nums = 1000
	changeBook2(&book1)
	fmt.Println(book1)

	p :=&Person{"Mike",23,"Beijing"}
	fmt.Println(p)
	var p2 Person
	p2 = Person{"Bob",23,"Shenzhen"}

	fmt.Println(p2)
	inter :=Interval{Start:2,End:4}
	fmt.Println(inter)


}