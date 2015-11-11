# Fibonacci numbers module

from textstat.textstat import textstat

import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
import string
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

import tools
import redability
import descriptive
import wordInformation



def text(text):
    #print(text)
    pl = pylinguistics()
    return pl.text(text)

class pylinguistics:

    def __init__(self):
        return None

    def text(self, text):
        self.language="en"
        self.tokens=[]
        self.postag=[]

        self.text = text.decode('utf-8','ignore')
        self.tokens = tools.getTokens(text)
        self.postag = tools.getPosTag(self)

        self.number_diff_words = 0 #to be calculated
        #should frequency and top words be included?

        self.word_count = descriptive.word_count(self)
        self.sentence_count = descriptive.sentence_count(self)
        self.avg_word_per_sentence = descriptive.avg_word_per_sentence(self)
        self.syllable_count = descriptive.syllable_count(self)    
        self.avg_syllables_per_word = descriptive.avg_syllables_per_word(self)


        return self
        
    def setLanguage(strLanguage):
        self.language=strLanguage


    def summary(self):

        print ('1. Descriptive')
        print ('  Word count=%i' %self.word_count)
        print ('  Sentence count=%i' %self.sentence_count)
        print ('  Syllable count=%i' % self.syllable_count)
        print ('  Avg word per sentence=%f'%self.avg_word_per_sentence)
        print ('  Avg syllable per word=%f' % self.avg_syllables_per_word)

        print ('2. Word Information')
        print ('  Adjective incidence=%f' % wordInformation.adjectiveIncidence(self))
        print ('  Noun incidence=%f' % wordInformation.nounIncidence(self))
        print ('  Verb incidence=%f' % wordInformation.verbIncidence(self))

        print ('3. Syntactic Pattern Density')
        print ('  Content density=%f' % self.contentDensity())

        print ('4. Redability')
        print ('  min(flesch_kincaid, coleman_liau)= %f' % redability.redability(self))
        print ('  Ambiquity=%f' % redability.calcAmbiquity(self))

        print (self.postag)





    ###################################
    ##### Syntactic Pattern Density ###
    ###################################


    def contentDensity(self):
        if (self.postag == []):
            self.postag= tools.getPosTag(self.tokens)
        
        nVerb=0
        nNoun=0
        nAdjective=0
        nAdverb=0
        
        for tag in self.postag:
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
        function_words = float(len(self.postag)-content_words)
        
        content_density = content_words / function_words if function_words else 0
            
        return content_density

    




