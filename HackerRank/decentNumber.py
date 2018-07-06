import itertools
t = input()
for p in xrange(t):
	n = input()
	uplimit = 10 ** n
	lowlimit = 10 ** (n - 1)
	large = -1
	for i in xrange(lowlimit, uplimit):
		s = str(i)
		l = len(s)
		count5 = s.count('5')
		count3 = s.count('3')
		if count3 + count5 == l:
			if (count5 % 3 == 0 and count5 > 0):
				if(count3 > 0 and count3 % 5 !=0):
					continue
				large = max(i, large)

			if (count3 % 5 == 0 and count3 > 0):
				if(count5 > 0 and count5 % 3 !=0):
					continue
				large = max(i, large)

	print large