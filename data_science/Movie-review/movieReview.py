import sklearn.datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn import metrics

review_train = sklearn.datasets.load_files('/home/Gokul/Documents/dataScience/Movie review/review_train', decode_error='ignore', encoding='utf-8')

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(review_train.data)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, review_train.target)

"""Naive Bayesian classification"""
#text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
#text_clf = text_clf.fit(review_train.data, review_train.target)

"""SVM classification"""
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42))])
_ = text_clf.fit(review_train.data, review_train.target)

docs_new = ['It was excellent', 'The movie was superb', 'The movie was exciting', 'The performance was simply stupid', 'I could do better things than watching the movie', 'It was a dump movie', 'Acting was good direction was not up to the mark', 'Acting was good direction was bad']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
	print('%r => %s' % (doc, review_train.target_names[category]))

review_test = sklearn.datasets.load_files('/home/Gokul/Documents/dataScience/Movie review/review_test', decode_error='ignore', encoding='utf-8')
docs_test = review_test.data
predicted = text_clf.predict(docs_test)
accuracy = np.mean(predicted == review_test.target)

print "\nAccuracy: ",accuracy

#print(metrics.classification_report(review_test.target, predicted, target_names=review_test.target_names))