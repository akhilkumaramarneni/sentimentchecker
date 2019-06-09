
[1st method] taking lexicon as all words(a-z)
and making true and false
module used - ml_features accuracy - 38.95 using linear SVC
									 38.78 using logistic regression
									 
									 same as using True and flase == 0/1(ml_features ieyh 0/1)
									 same accuracy

features set stored in features.pickle(True/false)
features set stored in features_with_0_1(0/1)


[2nd method] feature reduction
sentence(all emotions if present in lexicon(a-z) only took)
module used - ml_features_reduction -   39.95 using linear SVC
									     37.78 using logistic regression
									
									
									
features stored in features_reduction_0_1.pickle(0/1)  -39.711 logistic regression

