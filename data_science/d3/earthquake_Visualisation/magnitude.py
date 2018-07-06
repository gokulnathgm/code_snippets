import csv
file1 = open("earthquakes.csv")
file2 = open("magnitudes.csv", "a")
writer = csv.writer(file2)

count = 0
oldYear = None

for row in file1:
	spl = row.split(',')
	thisYear =  spl[0][:4]

	if thisYear == 'date':
		continue

	if oldYear and oldYear != thisYear:
		lis = [oldYear, count]
		writer.writerow(lis)

		count = 0

	oldYear = thisYear
	count += 1

if oldYear != None:
	lis = [oldYear, count]
	writer.writerow(lis)

file1.close()
file2.close()