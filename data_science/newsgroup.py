import sklearn.datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

twenty_train = sklearn.datasets.load_files('/home/Gokul/Documents/my-snippets/data_science/20news-bydate/20news-bydate-train', decode_error='ignore', encoding='utf-8')

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

"""Naive Bayesian classification"""
#text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
#text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

"""SVM classification"""
# text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42))])
# _ = text_clf.fit(twenty_train.data, twenty_train.target)

"""Grid Search"""
parameters = {'vect__ngram_range': [(1, 1), (1, 2)], 'tfidf__use_idf': (True, False), 'clf__alpha': (1e-2, 1e-3)}
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(twenty_train.data, twenty_train.target)

# docs_new = ['God is love', 'OpenGL on the GPU is fast', 'An apple a day keeps away the doctor', 'pen is mightier than sword', 'smoking is injurious to health']
docs_new = ['Former President and senior Congress leader Pranab Mukherjee will address the RSS workers here today. Pranab Mukherjee will participate in a program organized by the RSS-based Nagpur on June 7. The Indian Express reported quoting the senior RSS leader. Pranab Mukherjee&#39;s office information has not been confirmed yet. More than 600 RSS functionaries are expected to attend the event. We invited him inviting us to address RSS activists in Nagpur, which is going to take place at Headquarters. Senior RSS leader said that he accepted an invitation and agreed to participate in the event.']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
	print('%r => %s' % ('o/p', twenty_train.target_names[category]))

twenty_test = sklearn.datasets.load_files('/home/Gokul/Documents/my-snippets/data_science/20news-bydate/20news-bydate-test', decode_error='ignore', encoding='utf-8')
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
accuracy = np.mean(predicted == twenty_test.target)

print "\nAccuracy: ",accuracy

print(metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))