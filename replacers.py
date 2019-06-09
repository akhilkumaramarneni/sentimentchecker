from nltk.corpus import wordnet
from nltk.tag import pos_tag
import re

# first: replacing words like can't,won't and so on
replacement_patterns = [
    (r'won\'t', 'will not'),
    (r'can\'t', 'can not'),
    (r'i\'m', 'i am'),
    (r'ain\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would')
]
class RegexpReplacer(object):

    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            s = re.sub(pattern, repl, s)
        list_words = s.split(" ")
        repeatreplacer_object = RepeatReplacer()
        repeatless_words = [repeatreplacer_object.replace(word) for word in list_words]
        #print(repeatless_words)
        # universal pos tagging words
        if 'not' not in repeatless_words:
            return " ".join(repeatless_words)
        try:
            postagged_list = pos_tag(repeatless_words, tagset='universal')
            antonymreplacer_object = AntonymReplacer()
            replacedantonym_words = antonymreplacer_object.replace_negations(postagged_list)
            return " ".join(replacedantonym_words)
        except:
            return " ".join(repeatless_words)



# second: replace looove,ooooooh if not in wordnet
class RepeatReplacer(object):

    def __init__(self):
        self.repeat_regexp = re.compile(r'(.*)(.)\2(.*)')
        self.repl = r'\1\2\3'

    def replace(self, word):
        if wordnet.synsets(word):
            return word
        repl_word = self.repeat_regexp.sub(self.repl, word)
        #return repl_word+"akhil"
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word

# third : antonym replacer only not followed by adjective
class AntonymReplacer(object):

    def replace(self, word, pos=None):
        antonyms = set()
        for syn in wordnet.synsets(word, pos=pos):
            for lemma in syn.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
        if len(antonyms) >= 1:
            return antonyms.pop()
        else:
            return None

    # checking after not only adjectives replace remaining same
    def replace_negations(self, sent):
        i, l = 0, len(sent)
        words = []
        # print(sent)
        while i < l:
            word = sent[i][0]
            # print(l, i, word)
            if word == 'not' and i+1 < l and sent[i+1][1] == 'ADJ' :
                # print(word)
                ant = self.replace(sent[i+1][0])
                if ant:
                    words.append(ant)
                    i += 2
                    continue
            words.append(word)
            i += 1
        return words