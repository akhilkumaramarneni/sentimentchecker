from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from ml_features import pickle_analysis
import random
import pprint
import pickle


take_features_list = []  # set with all words in sentence
features_words = pickle_analysis()
#print(features_words)

def find_features(sentence):
    global take_features_list
    for word in sentence.split(" "):
        if word in features_words:
            take_features_list.append(word)

def pickle_sentence_analysis():
    pickle_all_sentences = ['anger_sentence.pickle', 'disgust_sentence.pickle',
                      'fear_sentence.pickle', 'joy_sentence.pickle', 'sad_sentence.pickle']
    global features_list
    for index, ph in enumerate(pickle_all_sentences):
        s = "pickled_algos/" + ph
        phares = open(s, "rb")
        [find_features(sent) for sent in pickle.load(phares)]

pickle_sentence_analysis()
take_features_list = list(set(take_features_list))

# features stored in take_features_list
# forming dataset

def find_dataset(sentence):
    words_tokenize = word_tokenize(sentence)
    fe_dict = {}
    ps = PorterStemmer()
    for w in take_features_list:
        if ps.stem(w) in words_tokenize:
            fe_dict[w] = 1
        else:
            fe_dict[w] = 0
    return fe_dict

features_list = []
def pickle_sentence_dataset():
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
        features_list = features_list + [(find_dataset(sent),cat) for sent in pickle.load(phares)]

    return features_list

data = pickle_sentence_dataset()
random.shuffle(data)

features = open("pickled_algos/features_reduction_0_1.pickle","wb")
pickle.dump(data, features)
features.close()

print(len(data))

