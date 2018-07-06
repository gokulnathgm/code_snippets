t = input()
for i in range(t):
	index = 0
	n = input()
	k = raw_input()
	a = k.split(' ')
	large = int(a[0])
	for j in range(n):
		a[j] = int(a[j])
		if a[j]>large:
			index = j
	
	noncontig = a[index]
	contig = a[index]
	for k in range(n):
		if a[k]>0 and k!=index:
			noncontig+=a[k]

	for k in range(0,n-1):
		total = a[k]
		for p in range(k+1,n):
			total+=a[p]
			if total>contig:
				contig = total

	print contig,
	print noncontig
