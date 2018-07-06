k = raw_input()
a = k.split(' ')
m = int(a[0])
n = int(a[1])

k = raw_input()
p = raw_input()
a = k.split(' ')
b = p.split(' ')

for i in range(m):
	a[i] = int(a[i])
for i in range(n):
	b[i] = int(b[i])

arr = []
arrbkp = []
q = 0

for k in range(m):
	for i in range(k,m):
		for j in range(q,n):
			if b[j] == a[i]:
				arrbkp.append(a[i])
				q = j+1
				break
	if len(arrbkp) > len(arr):
		arr = arrbkp[:]
	arrbkp = []

#swapping the array parameters
arrbkp = a[:]
a = b[:]
b = arrbkp[:]
arrbkp = []
c = m
m = n
n = c
q = 0

for k in range(m):
	for i in range(k,m):
		for j in range(q,n):
			if b[j] == a[i]:
				arrbkp.append(a[i])
				q = j+1
				break
	if len(arrbkp) > len(arr):
		arr = arrbkp[:]
	arrbkp = []

for i in arr:
	print i,