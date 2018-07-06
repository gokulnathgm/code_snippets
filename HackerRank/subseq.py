n = input()
a = []
for i in range(n):
	ent = input()
	a.append(ent)

leng = 1
for i in range(n-1):
	k = 1
	p = a[i]
	for j in range(i+1,n):
		if(a[j]>p):
			k+=1
			p = a[j]
	if(k>leng):
		leng = k
print leng