string = raw_input()
length = len(string)

frequency = [-1]*26
count = []

for i in range(length):
	frequency[ord(string[i])-97] = string.count(string[i])

for i in frequency:
	if i != -1:
		count.append(i)

print list(count)
temp = count[0]

boolean = True
flag = True

for i in count:
	if (i != temp):
		flag = False
		break

if flag == False:
	for i in range(len(count)):
		boolean = True
		count[i] = count[i] - 1
		if count[i] != 0:
			temp = count[i]

		print list(count),temp

		for j in count:
			if(j!=0 and j != temp):
				boolean = False
				count[i] = count[i] + 1
				temp = count[i]
				break

		if boolean == True:
			print "YES"
			break

if boolean == False:
		print "NO"

if flag == True:
		print "YES"