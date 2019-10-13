package main


import "fmt"


type Item interface{}

type treeNode struct{
	value Item
	left *treeNode
	right *treeNode
}


/*   
           A1
       B2        C3

    D4   E5    G7   I9

       F6         H8


*/

func main(){
	root :=treeNode{"A1",nil,nil}

	root.left = &treeNode{value:"B2"}
	root.right = &treeNode{value:"C3"}
	root.left.left = &treeNode{value:"D4"}
	root.left.right = &treeNode{value:"E5"}
	root.left.right.left = new(treeNode)
	root.left.right.left.value = "F6"
	 
	root.right.left = &treeNode{value:"G7"}
	root.right.left.right = &treeNode{value:"H8"}
	root.right.right = &treeNode{value:"I9"}

	root.PreOrder()
	root.Inorder()
	root.Postorder()

}


func (n *treeNode) PreOrder(){
	if n == nil{
		return
	}
	fmt.Println(n.value)
	n.left.PreOrder()
	n.right.PreOrder()
}



func (node *treeNode) Inorder(){
   if(node == nil){
      return
   }
   node.left.Inorder()
   fmt.Println(node.value)
   node.right.Inorder()
}



func (node *treeNode) Postorder(){
   if(node == nil){
      return
   }
   node.left.Postorder()
   node.right.Postorder()
   fmt.Println(node.value)
}
