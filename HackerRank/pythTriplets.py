t = input()
for p in range(t):
	n = input()
	count = 0
	c = 0
	m = 2
	total = 0

	while(True):
		for n in range(1,m):
			a = m*m - n*n
			b = 2 * m* n
			c = m*m + n*n

			#if(c > limit):
			#	break

			if 2*a - b == 1 or 2*a - b == -1 or 2*b -a == 1 or 2*b -a ==-1:
				total += c 
				count += 1

			print a, b, c

			if count == n:
				break

			print a, b, c

		m += 1

		if count == n:
			break		
	
	print total

		