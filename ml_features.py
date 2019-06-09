from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import random
import pprint
import pickle

features_list = []
features_words = []

def pickle_analysis():
    pickle_words = ['anger_words.pickle', 'disgust_words.pickle',
                      'fear_words.pickle', 'joy_words.pickle', 'sad_words.pickle'] 
    global features_words
    for index, ph in enumerate(pickle_words):
        s = "pickled_algos/" + ph
        phares = open(s, "rb")
        features_words = features_words + list(pickle.load(phares))
        phares.close()
    return features_words

#print(features_words)
#print(len(features_words))

# sentence to features sets
'''def find_features(sentence):
    words_tokenize = word_tokenize(sentence)
    fe_dict = {}
    ps = PorterStemmer()
    for w in features_words:
        if ps.stem(w) in words_tokenize:
            fe_dict[w] = 1
        else:
            fe_dict[w] = 0
        #fe_dict[w] = (ps.stem(w) in words_tokenize)

    return fe_dict

def pickle_sentence_analysis():
    pickle_all_sentences = ['anger_sentence.pickle', 'disgust_sentence.pickle',
                      'fear_sentence.pickle', 'joy_sentence.pickle', 'sad_sentence.pickle']
    global features_list
    for index, ph in enumerate(pickle_all_sentences):
        s = "pickled_algos/" + ph
        phares = open(s, "rb")
        if index == 0:
            cat = 'anger'
        elif index == 1:
            cat = 'disgust'
        elif index == 2:
            cat = 'fear'
        elif index == 3:
            cat = 'joy'
        elif index == 4:
            cat = 'sad'
        #print(pickle.load(phares))
        features_list = features_list + [(find_features(sent),cat) for sent in pickle.load(phares)]
        #features_words = features_words + list(pickle.load(phares))
        phares.close()
        #pprint.pprint(features_list)
        #break
    return features_list

pickle_analysis()  #features set
dataset = pickle_sentence_analysis()  #shufuling the features set
random.shuffle(dataset)

features = open("pickled_algos/features_with_0_1.pickle","wb")
pickle.dump(dataset, features)
features.close()

print(len(dataset))     '''



