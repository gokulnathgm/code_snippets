import json
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file = open("sentiment_score_reference.txt")
scores = {}
for line in file:
	word,score = line.split("\t")
	scores[word] = int(score)
file.close()

file = open("output.txt")
sentimentScore = open("sentiment_score_results.txt", 'a')
sid = SentimentIntensityAnalyzer()
for line in file:
	value = 0
	if line != '\n':
		parsed = json.loads(line)
		if 'text' in parsed.keys():
			lines = parsed['text'].encode('utf-8')
			words = lines.split()
			for word in words:
				if word in scores.keys():
					value = value + scores[word]
			output = ""
			sentimentScore.write(lines + "\n")
			sentimentScore.write("================================================================" + "\n")
			sentimentScore.write('Sentiment score: ' + str(value) + "\n" + "Polarity scores: ")
			ss = sid.polarity_scores(lines)
			for k in sorted(ss):
					output = output + '{0}: {1}, '.format(k, ss[k]*100)
			sentimentScore.write(output + "\n")
			sentimentScore.write("================================================================" + "\n\n\n\n\n")
sentimentScore.close()
file.close()