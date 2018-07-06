import itertools
t = input()
for k in range(t):
	inp = raw_input()
	a = inp.split(' ')
	n = int(a[0])
	m = int(a[1])
	a = []
	inp = raw_input()
	a = inp.split(' ')
	for i in range(n):
		a[i] = int(a[i])

	maxi = 0
	for i in range(1,n+1):
		arr = itertools.combinations(a,i)
		b = set(arr)
		for j in b:
			if (sum(j)%m)>maxi:
				maxi = sum(j)
print maxi