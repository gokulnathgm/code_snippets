string = raw_input()
length = len(string)

frequency = [0]*26
count = []

for i in string:
	frequency[ord(i)-97] += 1

for i in frequency:
	if i != 0:
		count.append(i)

maxOccur = 0
temp = 0
for i in count:
	maxi = count.count(i)
	if maxi > temp:
		temp = maxi
		maxOccur = i

diff = 0
for i in count:
	if i != maxOccur:
		diff += 1

if diff > 1:
	print "NO"

else:
	print "YES"