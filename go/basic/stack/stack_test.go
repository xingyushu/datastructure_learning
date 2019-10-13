package stack 

import "testing"


func TestStack(t *testing.T){
	stack :=New()
	if stack.Size()!=0 || !stack.IsEmpty(){
		t.Errorf("the size of stack is not equal 0")
	}

	stack.Push(1)
	stack.Push(3)

	if stack.Size()!=2 {
		t.Errorf("stack push failed!")
	}
	p :=stack.Pop()

	if v,ok :=p.(int);!ok||v!=3||stack.Size()!=1{
		t.Errorf("stack pop failed")
	}

	p2 :=stack.Peak()
	if v,ok :=p2.(int);!ok||v!=1||stack.Size()!=1{
		t.Log("stack peak error")
		t.Fail()
	}

	stack.Clear()
	if !stack.IsEmpty(){
		t.Errorf("stack clear error")
	}
}