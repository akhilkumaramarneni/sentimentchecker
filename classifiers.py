from sklearn.linear_model import LogisticRegression, SGDClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
from sklearn.naive_bayes import MultinomialNB
import pickle
import nltk


'''features_pickle = open("pickled_algos/features.pickle", "rb")
features_set = pickle.load(features_pickle)
features_pickle.close()  '''

'''features_pickle = open("pickled_algos/features.pickle", "rb")
features_set = pickle.load(features_pickle)
features_pickle.close()  '''

#from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier


features_pickle = open("pickled_algos/features_reduction_0_1.pickle", "rb")
features_set = pickle.load(features_pickle)
features_pickle.close()


train_set = features_set[:5200]
test_set = features_set[5200:]

#print(len(test_set))

# model = RandomForestClassifier(n_estimators=100)
#
# cv = cross_validation.KFold(len(features_set), n_folds=10, indices=False)
#
# # results = []
# # "Error_function" can be replaced by the error function of your analysis
# for traincv, testcv in cv:
#         probas = model.fit(features_set, features_set[traincv]).predict_proba(features_set[testcv])
#         results.append( akhil )


#classifier = nltk.NaiveBayesClassifier.train(train_set)
#print("Orginal Naive accuracy percent", nltk.classify.accuracy(classifier, test_set)*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(train_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, test_set))*100)


LinearSVC_classifier = SklearnClassifier(LinearSVC())
c=LinearSVC_classifier.train(train_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, test_set))*100)


MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(train_set)
print("MNB_classifier accuracy", nltk.classify.accuracy(MNB_classifier, test_set)*100)

'''


SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(train_set)
print("SGDClassifier accuracy percent:",nltk.classify.accuracy(SGDC_classifier, test_set)*100)
SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(train_set)
print("SVM", nltk.classify.accuracy(SVC_classifier, test_set)*100)   



# classifier.classify('features-set')  to predicting


'''