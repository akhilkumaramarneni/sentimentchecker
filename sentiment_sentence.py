from replacers import RepeatReplacer,RegexpReplacer
from keyword_analysis import emotion_count
from pharse_analysis import pharse_sentiment

#finding sentence input sentence
tofind_sentiment_sentence = "he Is Not good"
# read then from file such type of words
firstclause_emotion = ['than', 'as', 'because']
secondclause_emotion = ['but', 'so']

tofind_sentiment_sentence = " ".join([word.lower() for word in tofind_sentiment_sentence.split(" ")])
sentiment_wordslist = tofind_sentiment_sentence.split(" ")

# conjunctive present removing after that keyword
for conjuctive_word_index, conjuctive_word in enumerate(sentiment_wordslist):
    if conjuctive_word in firstclause_emotion:
        remove_sentence ='after'
    if conjuctive_word in secondclause_emotion:
        remove_sentence = 'before'

try:
    if(remove_sentence == 'after'):
        tofind_sentiment_sentence = " ".join(sentiment_wordslist[conjuctive_word_index:])
except:
    pass

# print(tofind_sentiment_sentence)
ob=RegexpReplacer()
replaced_after=ob.replace(tofind_sentiment_sentence)
#print(replaced_after)
dickeyword_count = emotion_count(replaced_after)  #keyword_analysis counter returned
dicpharse_count  = pharse_sentiment(replaced_after) #pharse_analysis counter returned
print(dickeyword_count.most_common(3))
print(dicpharse_count.most_common(3))


print("Overall emotion is anger")
