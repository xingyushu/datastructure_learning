package sort 

//冒泡排序
func  BubbleSort(arr[]int)[]int{
	var temp int
	if len(arr) <=1{
		return arr
	}

	for j :=len(arr);j>0;j--{
		for i :=0;i<len(arr);i++{
			if arr[i]>arr[i+1]{
				swap(arr,i,i+1)
			}
		}
	}
	return arr
}



//选择排序
func SelectSort(arr []int)[]int{
	if len(arr) <=1{
		return arr
	}

	for j :=len(arr);j>0;j--{
		max :=0
		for i :=1;i<len(arr);i++{
			if arr[i]>arr[max]{
				max = i
			}
		}
		swap(arr,max,j-1)
	}
}



//快速排序
func QuickSort(arr[]int) []int{
	if len(arr)<=1{
		return arr
	}

	mid :=arr[0]
	head,tail :=0,len(arr)-1

	for i :=1;i<tail{
		if arr[i]>mid{
			arr[i],arr[tail]=arr[tail],arr[i]
			tail--
		}else{
			arr[i],arr[head]=arr[head],arr[i]
			head++
			i++
		}
		QuickSort(arr[:head])
		QuickSort(arr[head+1:])
	}
	return arr
}


//插入排序
func InsertSort(arr []int)[]int{
	if len(arr)<2{
		return arr
	}

	for i :=1;i<len(arr);i++{
		for j :=i-1;j>=0;j--{
			if arr[j+1]<a[j]{
				swap(arr,j,j+1)
			}else{
				break
			}
		}
	}
}


func swap(arr[]int,i,j){
	var tmp int
	temp = arr[j]
	arr[j] = arr[i]
	arr[i] = temp	
}