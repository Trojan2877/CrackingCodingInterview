class count01:
	def compressed(self,str1):
		# sort string
		# count++ for each char unless char is changed
		sortedStr = sorted(str1)
		print(sortedStr)
		count = 0
		resultStr = ""
		for i in range(0,len(sortedStr)-1):
			if i == len(sortedStr)-2:
				if sortedStr[i] != sortedStr[i+1]:
					count = count + 1
					resultStr = resultStr + str(count)
					count = 0
					resultStr = resultStr + sortedStr[i]
					resultStr = resultStr + str(1)
					resultStr = resultStr + sortedStr[i+1]
				else :
					count = count + 2
					resultStr = resultStr + str(count)
					count = 0
					resultStr = resultStr + sortedStr[i]
			elif sortedStr[i] != sortedStr[i+1]:
				count = count + 1
				resultStr = resultStr + str(count)
				count = 0
				resultStr = resultStr + sortedStr[i]
			else:
				count = count + 1
		return resultStr


if __name__ == '__main__':
	obj1 = count01()
	str1 = input("enter string : \n")
	print(obj1.compressed(str1))	
