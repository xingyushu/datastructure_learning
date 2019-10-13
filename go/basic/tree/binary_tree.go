package tree

import "fmt"


type Item  interface{}


type Node struct{
	Key int
	Value Item
	left *Node
	right *Node
}


type BinarySearch interface{
	Insert(key int,value Item)
	Min() *Item
	Max() *Item
	Search(key int) bool
	PreOrder()
}

type ItemBinarySearchTree struct{
	Root *Node
}


func (bst *ItemBinarySearchTree) Insert(key int,value Item){
	n :=&Node{key,value,nil,nil}

	if bst.Root == nil{
		bst.Root =n
	}else{
		insertNode(bst.Root,n)
	}
}

func insertNode(node,n1 *Node){
	if n1.key < node.key{
		if node.left == nil{
			node.left = n1
		}else{
			insertNode(node.left,n1)
		}
	}else{
		insertNode(node.right,n1)
	}
}

func (bst *ItemBinarySearchTree) Min() *Item{
	n :=bst.Root

	if n == nil{
		return nil
	}

	for{
		if n.left == nil{
			return &n.Value
		}else{
			n = n.left
		}

	}
} 

func (bst *ItemBinarySearchTree) Max() *Item{
	n :=bst.Root

	if n == nil{
		return nil
	}

	for{
		if n.right == nil{
			return &n.Value
		}else{
			n = n.right
		}

	}
} 



func (bst *ItemBinarySearchTree) PreOrder(){
	n :=bst.Root
	if n == nil{
		return
	}
	fmt.Println(n.Value)
	n.left.PreOrder()
	n.right.PreOrder()
}