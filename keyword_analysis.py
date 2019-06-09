from nltk.stem import PorterStemmer
from collections import Counter
import pickle

# this return count of keyword emotions
# loading all set of emotion words
pickle_words =['anger_words.pickle', 'disgust_words.pickle',
               'fear_words.pickle', 'joy_words.pickle', 'sad_words.pickle']

anger_words = []
disgust_words = []
fear_words = []
joy_words = []
sad_words = []

for index,document in enumerate(pickle_words):
    s="pickled_algos/"+document
    words = open(s, "rb")
    # print(index,s)
    if index == 0:
        anger_words = list(pickle.load(words))
    elif index == 1:
        disgust_words = list(pickle.load(words))
    elif index == 2:
        fear_words = list(pickle.load(words))
    elif index == 3:
        joy_words = list(pickle.load(words))
    elif index == 4:
        sad_words = list(pickle.load(words))
    words.close()

ps_object = PorterStemmer()
count_list = []
counter_count =Counter()
#keyword analysis
def emotion_count(sentence):
    stem_sentence_words = [ps_object.stem(each) for each in sentence.split(" ")]
    for each in stem_sentence_words:
        if each in anger_words:
            count_list.append('anger')
        if each in joy_words:
            count_list.append('joy')
        if each in disgust_words:
            count_list.append('disgust')
            #print(each)
        if each in fear_words:
            count_list.append('fear')
        if each in sad_words:
            count_list.append('sad')

    for counting in count_list:
        counter_count[counting]+=1
    #print(dict(counter_count))
    return counter_count

#emotion_count("i am good")