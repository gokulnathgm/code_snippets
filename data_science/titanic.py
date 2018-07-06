import csv
	
def loadCSV(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	return dataset

def probabilitySurviving(dataset):
	l = len(dataset)
	count1 = 0
	count0 = 0
	age0 = 0
	age1 = 0
	maleSurvivors = 0
	femaleSurvivors = 0
	maleCount = 0
	femaleCount = 0
	for i in range(1,l):
		if dataset[i][1] == '1':
			count1 += 1
			#age1 += int(dataset[i][5])
			if dataset[i][4] == 'male':
				maleSurvivors += 1
			if dataset[i][4] == 'female':
				femaleSurvivors += 1

		if dataset[i][1] == '0':
			count0 += 1
			#age0 += int(dataset[i][5])

		if dataset[i][4] == 'male':
			maleCount += 1

		if dataset[i][4] == 'female':
			femaleCount += 1


	probSurvive = count1 / float((count1 + count0))
	probNotSurvive = count0 / float((count0 + count1))
	probMaleSurvivors = maleSurvivors / float(count1)
	probFemaleSurvivors = femaleSurvivors / float(count1)
	probMale = maleCount / float(l)
	probFemale = femaleCount / float(l)
	#probAgeSurvive = age1 / float((age1 + age0))
	#probAge = 

	Mprobability = probMaleSurvivors * probSurvive / probMale
	Fprobability = probFemaleSurvivors * probSurvive / probFemale

	print "Proabability that a male will survive: ", Mprobability
	print "Prorbability that a female will survive: ", Fprobability
	
filename = "titanic_train.csv"
dataset = loadCSV(filename)
probabilitySurviving(dataset)