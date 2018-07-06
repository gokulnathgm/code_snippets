def recurse(n):
	if (n == 0):
		return
	recurse(n - 1)
	print n

recurse(5)