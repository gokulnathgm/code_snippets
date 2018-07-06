s = raw_input()
a = s.split(' ')
n = len(a)
maxtotal = max(a, key=lambda p:int(p))
total = 0
for i in range(n):
	total+=int(a[i])
	if(total < 0):
		total = 0
	elif total > maxtotal:
		maxtotal = total
print maxtotal