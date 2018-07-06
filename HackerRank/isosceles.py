t = input()
for p in range(t):
	n = input()
	count = 0
	total = 0
	i = 5
	
	while(True):
		for j in range(1,i):
			for k in range(1,j):
				if i*i == j*j + k*k:
					if k == 2*j + 1 or k == 2*j - 1 or j == 2*k +1 or j == 2*k -1:
						count += 1
						total += i
				if count == n:
					break
			if count == n:
				break

		i +=1
		if count == n:
			print total
			break






