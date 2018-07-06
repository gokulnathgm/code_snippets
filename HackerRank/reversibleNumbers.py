t = input()
for p in range(t):
	n = input()
	count = 0
	for i in range(10,n):
		if i % 10 == 0:
			continue
		flag = True
		num1 = str(i)
		num2 = num1[::-1]

		num1 = int(num1)
		num2 = int(num2)

		total = num1 + num2
		total = str(total)

		for j in total:
			k = int(j)
			if(k % 2 == 0):
				flag = False
				break

		if flag == True:
			count += 1

	print count
