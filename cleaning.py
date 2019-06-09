from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import pickle

# cleaning all emotion words
with open("unclean_words.txt",'r') as f:
    read_data = f.read()
    for line in read_data.split("\n"):
        try:
            if((int)(line)>1):
                pass
        except:
            f2 = open('cleaned_words.txt','a')
            f2.write(line)
            f2.write("\n")

# finding wmotion words with synonyms,lemmsa and picking all words
anger_words = []
anticipation_words = []
disgust_words = []
fear_words = []
joy_words = []
sadness_words = []
surprise_words = []
trust_words = []
emotions_list = [anger_words, anticipation_words, disgust_words, fear_words,
                 joy_words, sadness_words, surprise_words, trust_words]

with open("cleaned_words.txt", 'r') as f:
    read_data = f.read()
    for line in read_data.split("\n"):
        # print(line)
        positive_index = line.find('positive')
        negative_index = line.find('negative')
        if(positive_index == -1 or negative_index == -1 or
               (line[positive_index+9] == '0' and line[negative_index+9] == '0')):
           pass
        else:
            words_list = line.split(" ")
            emotions_words = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
            for index, value in enumerate(emotions_words):
                if(words_list[index+3].startswith(value) and words_list[index+3].endswith('1')):
                    emotions_list[index].append(words_list[0])
                    # adding synonyms
                    #for syn in wordnet.synsets(words_list[0]):
                        # print("syn:",syn)
                        #for l in syn.lemmas():
                            # print("l:", l)
                            #emotions_list[index].append(l.name())

# stemming those words makes less redundent (Portors algorithm)
stemmer_object = PorterStemmer()
anger_words_set = set([stemmer_object.stem(word) for word in emotions_list[0]])
# anticipation_words_set = set([stemmer_object.stem(word) for word in emotions_list[1]])
disgust_words_set = set([stemmer_object.stem(word) for word in emotions_list[2]])
fear_words_set = set([stemmer_object.stem(word) for word in emotions_list[3]])
joy_words_set = set([stemmer_object.stem(word) for word in emotions_list[4]])
sadness_words_set = set([stemmer_object.stem(word) for word in emotions_list[5]])
# surprise_words_set = set([stemmer_object.stem(word) for word in emotions_list[6]])
# trust_words_set = set([stemmer_object.stem(word) for word in emotions_list[7]])

# picking all sets of emotion words
save_angerwords = open("pickled_algos/anger_words.pickle","wb")
pickle.dump(anger_words_set, save_angerwords)
save_angerwords.close()

save_disgustwords = open("pickled_algos/disgust_words.pickle","wb")
pickle.dump(disgust_words_set, save_disgustwords)
save_disgustwords.close()

save_fearwords = open("pickled_algos/fear_words.pickle","wb")
pickle.dump(fear_words_set, save_fearwords)
save_fearwords.close()

save_joywords = open("pickled_algos/joy_words.pickle","wb")
pickle.dump(joy_words_set, save_joywords)
save_joywords.close()

save_sadwords = open("pickled_algos/sad_words.pickle","wb")
pickle.dump(sadness_words_set, save_sadwords)
save_sadwords.close()


# print(anger_words_set)
# print(anticipation_words_set)
# print(disgust_words_set)
# print(fear_words_set)
# print(joy_words_set)

''' l=0
for i in emotions_list:
    print(i,emotions_words[l])
    l=l+1  '''


