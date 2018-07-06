t = input()
for i in range(t):
	a = []
	n = input()
	a = map(int, raw_input().split())
	contig = a[0]
	total = a[0]
	for j in range(1,n):
		total = max(a[j], total+a[j])
		contig = max(contig, total)
			
	total = 0
	negativecount = 0
	if(a[0] < 0):
		negativemax = a[0]
	for j in range(0,n):
		if a[j] >= 0:
			total += a[j]
		elif a[0] < 0:
			negativecount += 1
			if(a[j] > negativemax):
				negativemax = a[j]
	if negativecount == n:
		noncontig = negativemax
	else:
		noncontig = total

	print contig,
	print noncontig