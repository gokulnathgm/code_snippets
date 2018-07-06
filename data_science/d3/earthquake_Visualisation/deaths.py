import csv
file1 = open("quakes.csv")
file2 = open("deaths.csv", "a")
writer = csv.writer(file2)

count = 0
oldYear = None

for row in file1:
	spl = row.split('\t')
	thisYear =  spl[2]

	if thisYear == 'YEAR' or int(thisYear) < 0:
		continue

	if oldYear and oldYear != thisYear:
		if count != 0:
			lis = [oldYear, count]
			writer.writerow(lis)

		count = 0

	oldYear = thisYear
	if spl[23] != "":
		count += int(spl[23])

if oldYear != None:
	if count != 0:
		lis = [oldYear, count]
		writer.writerow(lis)

file1.close()
file2.close()