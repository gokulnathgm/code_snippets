n = input()
s = raw_input()
a = s.split(' ')
a = map(int, a);

n = input()
s = raw_input()
b = s.split(' ')
b = map(int, b);

arr = []

for i in a:
	if i in b:
		if a.count(i) != b.count(i):
			arr.append(i)
	else:
		arr.append(i)

for i in set(arr):
	print i,