#coding:utf-8

from stack import Stack   

def inTopre(prefix):
	prec = dict()
	prec[')'] = 4
	prec['*'] = 3
	prec['/'] = 3
	prec['+'] = 2
	prec['-'] = 2
	prec['('] = 1
	prefix_expr = []
	s = Stack()
	for item in reversed(prefix.split()):
		if item not in "*/+-()":
			prefix_expr.append(item)
		elif item == ")":
			s.push(item)
		elif item == "(":
			while s.peek()!=")":
				prefix_expr.append(s.pop())
				s.pop()
		else:
			while (not s.isEmpty()) and s.peek()!=")" and prec[s.peek()]>prec[item]:
				prefix_expr.append(s.pop())
				s.push(item)
			s.push(item)
	while not s.isEmpty():
		prefix_expr.append(s.pop())

	prefix_expr.reverse()
	return ' '.join(prefix_expr)


def  cal(prefix):
	s2 = Stack()
	result = []
	for item in reversed(prefix.split()):
		if item not in "+-*/":
			s2.push(item)
		else:
			op1 = int(s.pop())
			op2 = int(s.pop())
			print(op1,item,op2)
			result.append(op(item,op1,op2))
	return result



def op(op,op1,op2):
	if op == "+":
		return op1+op2
	elif op == "-":
		return op1-op2
	elif op == "*":
		return op1*op2
	elif op == "/":
		return op1/op2
	else:
		raise Exception("Error operation")


infix_str = '1+((2+3)*4)-5'
prefix_output = inTopre(infix_str)
print(infix_str)
print(prefix_output)
prefix_result = cal(prefix_output)
print(prefix_result)