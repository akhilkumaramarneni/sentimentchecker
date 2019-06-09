from nltk.tag import pos_tag
from collections import Counter
import pickle



def pharse_sentiment(sent):
    sent_list = sent.split(" ")
    allowed_types = ['NOUN', 'ADJ', 'VERB', 'ADV']
    pos_tag_list = pos_tag(sent_list, tagset='universal')
    allowed_pos_tag = [word[0] for word in pos_tag_list if word[1] in allowed_types]
    #xprint(allowed_pos_tag)
    sentence_bigrams = [[allowed_pos_tag[i], allowed_pos_tag[i+1]] for i in range(len(allowed_pos_tag)-1)]

    return pickle_analysis(sentence_bigrams)

def pickle_analysis(bigrams):
    pickle_pharses = ['anger_pharse.pickle', 'disgust_pharse.pickle',
                      'fear_pharse.pickle', 'joy_pharse.pickle', 'sad_pharse.pickle']
    for index, ph in enumerate(pickle_pharses):
        s = "pickled_algos/" + ph
        phares = open(s, "rb")
        if index == 0:
            anger_phares = pickle.load(phares)
        elif index == 1:
            disgust_phares = pickle.load(phares)
        elif index == 2:
            fear_phares = pickle.load(phares)
        elif index == 3:
            joy_phares = pickle.load(phares)
        elif index == 4:
            sad_phares = pickle.load(phares)

        phares.close()

    #analysis phase

    list_analysis = []
    for list_in in bigrams:
        if list_in in joy_phares:
            list_analysis.append('joy')
        if list_in in disgust_phares:
            list_analysis.append('disgust')
        if list_in in anger_phares:
            list_analysis.append('anger')
        if list_in in sad_phares:
            list_in.append('sad')
        if list_in in fear_phares:
            list_in.append('fear')

    counter_count = Counter()
    for counting in list_analysis:
        counter_count[counting]+=1
    return counter_count


#print(pharse_sentiment("this is an good greeted apple"))