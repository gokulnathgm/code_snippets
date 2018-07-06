t = input()
for p in range(t):
	s = raw_input()
	a = s.split(' ')
	n = int(a[0])
	m = int(a[1])
	s = raw_input()
	a = s.split(' ')

	total = 0
	temp = 0
	for i in range(n):
		temp = (temp + int(a[i])) % m
		if temp > total:
			total = temp
		a[i] = temp

	#sorts the indexes of list 'a'
	b = sorted(range(len(a)), key=lambda k:a[k])
	
	a.sort()

	for i in range(1,n):
		if b[i] < b[i-1]:
			temp = (int(a[i-1]) - int(a[i])) % m
			if(temp > total):
				total = temp
	print total