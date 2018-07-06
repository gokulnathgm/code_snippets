print "Enter the size of the queue"
n = input()
a = [None]*n
front = -1
rear = -1
while(True):
	print "\n\n1.Insert 2.Delete 3.View 4.Exit"
	choice = input()

	if choice == 1:
		print "\nenter the elements seperated by newline, -999 to stop"
		while(True):	
			num = input()
			if num == -999:
				break
			if rear == n:
				rear = 0
			if rear == front != -1 and a.count(None)==0:
				print "\nqueue overflows"
				break
			else:
				if front == -1:
					front = 0
				if rear == -1:
					rear = 0
				a[rear] = num
				rear+=1

	if choice == 2:
		if front == -1 or a.count(None)==n:
			print "\nqueue underflows"
			"""if front == rear:
			front = rear = -1"""
		elif front == n:
			front = 0
			print "deleted"
			a[front] = None
			front+=1
		else:
			print "deleted"
			a[front] = None
			front+=1

	if choice == 3:
		print front,rear
		for i in a:
			print i,

	if choice == 4:
		break