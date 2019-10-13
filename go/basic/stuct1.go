package main  

import "fmt"

type  Book struct{
	Title string  
	Nums  int 
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

}