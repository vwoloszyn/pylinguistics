# Fibonacci numbers module

from textstat.textstat import textstat

import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
import string
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords



def text(text):
    #print(text)
    pl = pylinguistics()
    return pl.text(text)
    

class pylinguistics:

    def __init__(self):
                return None

    def text(self, text):
        self.number_diff_words = 0 #to be calculated
        #should frequency and top words be included?
        self.text = text
        self.word_count = self.word_count(text)
        self.sentence_count = self.sentence_count(text)
        self.avg_word_per_sentence = self.avg_word_per_sentence()
        self.syllable_count = self.syllable_count(text)    
        self.avg_syllables_per_word = self.avg_syllables_per_word(text)
        return self
        


    def summary(self):
        print ('word count =%i' %self.word_count)
        print ('sentence count =%i' %self.sentence_count)
        print ('avg word per sentence =%f'%self.avg_word_per_sentence)
        print ('syllable count =%i' % self.syllable_count)
        print ('avg syllable per word =%f' % self.avg_syllables_per_word)




    def avg_word_per_sentence (self):
        x=0
        try:
            x= self.word_count / self.sentence_count
        except:
            x=0
        return x
                    
    def avg_syllables_per_word (self,texto):
        x=0
        try:
            x= textstat.avg_syllables_per_word(self,texto)
        except:
            x=0
        return x

    def word_count (self,texto):
        from nltk.tokenize import RegexpTokenizer
        x=0
        try:
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(texto)
            x= len(tokens)
        except:
            x=0
        return x

    def sentence_count (self, texto):
        x=0
        try:
            x= textstat.sentence_count(texto)
        except:
            x=0
        return x

    def syllable_count (self,texto):
        x=0
        try:
            x= textstat.syllable_count(texto)
        except:
            x=0
        return x

    ##METRICAS

    def redability(self): 
        return min(self.calc_flesch_kincaid_grade(), self.calc_coleman_liau_index())

    def calc_coleman_liau_index (self):
        texto = self.text.decode('utf-8','ignore')
        x=0
        try:
            x= textstat.coleman_liau_index(texto)
        except:
            x=0
        return x

    def calc_flesch_kincaid_grade (self):
        texto = self.text.decode('utf-8','ignore')
        x=0
        try:
            ASL = textstat.avg_sentence_length(texto)
            ASW = textstat.avg_syllables_per_word(texto)
            FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
            x= round(FKRA, 1)
        except:
            x=0
        return x

    def contentDensity(self):
        sentence = self.text.decode('utf-8','ignore')
        tokens = nltk.word_tokenize(sentence)

        #check lenght words
        tokens = [w.lower() for w in tokens if len(w)<20]

        #stopwordremoval
        #stop = stopwords.words('english')
        #tokens = [w.lower() for w in tokens if w not in stop]

        postag= nltk.pos_tag(tokens)
        
        nVerb=0
        nNoun=0
        nAdjective=0
        nAdverb=0
        
        for tag in postag:
            word = tag[0]
            word_clas = tag[1]
            if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
                nVerb +=1
            elif word_clas == "NN" or word_clas == "NNS" or word_clas == "NNP" or word_clas == "NNPS" :
                nNoun +=1
            elif word_clas == "JJ" or word_clas == "JJR" or word_clas == "JJS" :
                nAdjective +=1
            elif word_clas == "RB" or word_clas == "RBR" or word_clas == "RBS":
                nAdverb +=1
        
        contentDensity=10
        #print ('somatorio %i'%(nVerb+nNoun+nAdjective+nAdverb))
        #print ('dividido por %i'%len(postag))
    
        content_words = nVerb+nNoun+nAdjective+nAdverb
        function_words = float(len(postag)-content_words)
        
        content_density = content_words / function_words if function_words else 0
            
        return content_density

    def calcAmbiguidade(self):
        sentence = self.text.decode('ascii','ignore')
        tokens = nltk.word_tokenize(sentence)

        #check lenght words
        tokens = [w.lower() for w in tokens if len(w)<20]

        #stopwordremoval
        #stop = stopwords.words('english')
        #tokens = [w.lower() for w in tokens if w not in stop]

        postag= nltk.pos_tag(tokens)


        nVerb=0
        nNoun=0
        nAdjective=0
        nAdverb=0

        mVerb=0
        mNoun=0
        mAdjective=0
        mAdverb=0

        avgMVerb = 0
        avgMNoun = 0
        avgMAdjective = 0
        avgMAdverb = 0

        AvgAmbiquity = 0


        #Tag Meaning
        #https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

        for tag in postag:
            word = tag[0]
            word_clas = tag[1]
            #print(word_clas)
            if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
                nVerb +=1
                mVerb += len(wn.synsets(word))
            elif word_clas == "NN" or word_clas == "NNS" or word_clas == "NNP" or word_clas == "NNPS" :
                nNoun +=1
                mNoun += len(wn.synsets(word))
            elif word_clas == "JJ" or word_clas == "JJR" or word_clas == "JJS" :
                nAdjective +=1
                mAdjective += len(wn.synsets(word))
            elif word_clas == "RB" or word_clas == "RBR" or word_clas == "RBS":
                nAdverb +=1
                mAdverb += len(wn.synsets(word))


        if nVerb > 0: avgMVerb =  mVerb / float(nVerb)
        if nNoun > 0: avgMNoun = mNoun / float(nNoun)
        if nAdjective > 0: avgMAdjective = mAdjective / float(nAdjective)
        if nAdverb > 0: avgMAdverb = mAdverb / float(nAdverb)

        if (nVerb+nNoun+nAdjective+nAdverb) > 0: AvgAmbiquity = (mVerb+mNoun+mAdjective+mAdverb) / float(nVerb+nNoun+nAdjective+nAdverb)
        return AvgAmbiquity





