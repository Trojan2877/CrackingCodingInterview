class count:

	def compressed(self,str1):
		countList = [0] * 200
		resultStr = ""
		for s in str1:
			countList[ord(s)] = countList[ord(s)] + 1
		for s in str1:
			if countList[ord(s)] != -1:
				resultStr = resultStr + s + str(countList[ord(s)])
				countList[ord(s)] = -1
		return resultStr

if __name__ == '__main__':
	obj1 = count()
	str1 = input("enter string : \n")
	print(obj1.compressed(str1))