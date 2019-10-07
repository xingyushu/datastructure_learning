#coding:utf-8


def test(s1,s2):
	alist = list(s2)
	pos1 = 0
	ok = True
	while pos1<len(s1) and ok:
		pos2  = 0 
		found = False 
		while pos2 <len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 = pos2+1

		if found:
			alist[pos2] = None
			pos1 = pos1+1
		else:
			ok = False
	return ok and (len(filter(None, alist)) == 0)


def main():
	print(test("abcdd","bcad2"))


if __name__ == "__main__":
	main()



