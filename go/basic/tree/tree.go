package main  

import "fmt"


//定义树的结构
type Node struct{
	le *Node 
	data interface{}
	ri *Node
}


func NewNode(left,right *Node) *Node{
	return &Node{left,nil,right}
}


func (n *Node) SetData(data interface{}){
	n.data = data
}

func main(){
	root :=NewNode(nil,nil)
	root.SetData("root")
	l :=NewNode(nil,nil)
	l.SetData("left")
	r :=NewNode(nil,nil)
	r.SetData("right")
	root.le = l
	root.ri = r
	fmt.Printf("%v\n",root)
}