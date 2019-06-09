from replacers import RegexpReplacer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import pickle

joy_sentence = []
disgust_sentence = []
fear_sentence = []
sad_sentence = []
anger_sentence = []

with open("second_dataset.txt", 'r') as f:
    read_data = f.read()
    for line in read_data.split("\n"):
        # print(line)
        list_sentence = line.split("|")
        #print(list_sentence)
        if list_sentence[36] == 'joy':
            joy_sentence.append(list_sentence[40])
        elif list_sentence[36] == 'disgust':
            disgust_sentence.append(list_sentence[40])
        elif list_sentence[36] == 'fear':
            fear_sentence.append(list_sentence[40])
        elif list_sentence[36] == 'anger':
            anger_sentence.append(list_sentence[40])
        elif list_sentence[36] == 'sadness':
            sad_sentence.append(list_sentence[40])

#lowering function for sentences
def lowring_words(emotion_sentence):

    lower_sentences = []
    for sentence in emotion_sentence:
        lower_words = []
        for word in sentence.split(" "):
            if word.isalpha():
                lower_words.append(word.lower())
        lower_sentences.append(" ".join(lower_words))

    return lower_sentences

joy_sentence_lower = lowring_words(joy_sentence)
disgust_sentence_lower = lowring_words(disgust_sentence)
fear_sentence_lower = lowring_words(fear_sentence)
sad_sentence_lower = lowring_words(sad_sentence)
anger_sentence_lower = lowring_words(anger_sentence)

#replacing sentences
def pass_replacer(sent):
    replace_sentence = []
    replacer_object = RegexpReplacer()
    for sentence in sent:
        replace_sentence.append(replacer_object.replace(sentence))
    return replace_sentence

#print(joy_sentence_lower)
joy_sentence_replace = pass_replacer(joy_sentence_lower)
#print(joy_sentence_replace)
disgust_sentence_replace = pass_replacer(disgust_sentence_lower)
anger_sentence_replace = pass_replacer(anger_sentence_lower)
fear_sentence_replace = pass_replacer(fear_sentence_lower)
sad_sentence_replace = pass_replacer(sad_sentence_lower)

# pickle sentences also

save_angersentence = open("pickled_algos/anger_sentence.pickle","wb")
pickle.dump(anger_sentence_replace, save_angersentence)
save_angersentence.close()

save_joysentence = open("pickled_algos/joy_sentence.pickle","wb")
pickle.dump(joy_sentence_replace, save_joysentence)
save_joysentence.close()

save_disgustsentence = open("pickled_algos/disgust_sentence.pickle","wb")
pickle.dump(disgust_sentence_replace, save_disgustsentence)
save_disgustsentence.close()

save_fearsentence = open("pickled_algos/fear_sentence.pickle","wb")
pickle.dump(fear_sentence_replace, save_fearsentence)
save_fearsentence.close()

save_sadsentence = open("pickled_algos/sad_sentence.pickle","wb")
pickle.dump(sad_sentence_replace, save_sadsentence)
save_sadsentence.close()



#allowing types NOUN,ADJ,VERB,ADV
'''
 1st cleanning we need entire code, second for ml_features below no need just sentences is enough 
 
def allowing_words_sentences(lowered_sentences):

    allowed_types = ['NOUN', 'ADJ', 'VERB', 'ADV']
    allowed_sentences = []
    for sentence in lowered_sentences:
        list_words = [word for word, type in pos_tag(word_tokenize(sentence), tagset='universal') if type in allowed_types]
        allowed_sentences.append(" ".join(list_words))

    return allowed_sentences

# bigrams forming
def bigram_phares(sent):
    sent = allowing_words_sentences(sent)
    list_bigrams = []
    for sentence in sent:
        split_list = sentence.split(" ")
        for i in range(len(split_list)-1):
            local_list = []
            local_list.append(split_list[i])
            local_list.append(split_list[i + 1])
            list_bigrams.append(local_list)

    return list_bigrams

# pharse with bi-grams only
save_joypharse = open("pickled_algos/joy_pharse.pickle","wb")
pickle.dump(bigram_phares(joy_sentence_replace), save_joypharse)
save_joypharse.close()

save_disgustpharse = open("pickled_algos/disgust_pharse.pickle","wb")
pickle.dump(bigram_phares(disgust_sentence_replace), save_disgustpharse)
save_disgustpharse.close()

save_angerpharse = open("pickled_algos/anger_pharse.pickle","wb")
pickle.dump(bigram_phares(anger_sentence_replace), save_angerpharse)
save_angerpharse.close()

save_fearpharse = open("pickled_algos/fear_pharse.pickle","wb")
pickle.dump(bigram_phares(fear_sentence_replace), save_fearpharse)
save_fearpharse.close()

save_sadpharse = open("pickled_algos/sad_pharse.pickle","wb")
pickle.dump(bigram_phares(sad_sentence_replace), save_sadpharse)
save_sadpharse.close()                          '''




'''data = urllib.request.urlopen('https://raw.githubusercontent.com/sinmaniphel/py_isear_dataset/master/isear.csv')
file_save = open('second_dataset.txt','w')
file_save.write(str(data.read()))
file_save.close()                                               
# print(data.read())    '''

'''with open("second_dataset.txt",'r') as f:
    read_data = f.read()
    for line in read_data.split("\n"):
        file_save = open('clean_second_data.txt','w')
        file_save.write(line)
        file_save.write("\n")
        file_save.close()
        break '''
