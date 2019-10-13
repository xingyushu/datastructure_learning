package stack 

type Stack struct{     //定义栈
	dataStore  []interface{}
	size int
}

func New() *Stack{   // 栈初始化
	s :=new(Stack)
	s.dataStore = make([]interface{},0)
	s.size = 0

	return s 
}

func (s *Stack) Size() int{   //返回栈的大小
	return s.size
}

func (s *Stack) IsEmpty() bool{  //判断栈是否为空
	return s.size == 0
}


func (s *Stack) Push(element interface{}){   //数据入栈操作
	s.dataStore = append(s.dataStore,element)
	s.size++
}


func (s *Stack) Pop() interface{} {   //数据出栈操作
	if(s.IsEmpty()){
		return nil
	}
	last :=s.dataStore[s.Size()-1]
	s.dataStore = s.dataStore[:s.Size()-1]
	s.size--
	return last

}


func (s *Stack) Peak() interface{} {  //取栈顶元素
	if(s.IsEmpty()){
		return nil
	}
	return s.dataStore[s.Size()-1]
}

func (s *Stack) Clear(){   //清空栈元素

	s.dataStore=s.dataStore[:1]
	s.size = 0 
}
