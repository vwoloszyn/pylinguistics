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



def text(text):
    #print(text)
    pl = pylinguistics()
    return pl.text(text)
    

class pylinguistics:

    def __init__(self):
                return None

    def text(self, text):
        self.idiom="en"
        self.tokens=[]
        self.postag=[]

        self.number_diff_words = 0 #to be calculated
        #should frequency and top words be included?
        self.text = text.decode('utf-8','ignore')
        self.word_count = self.word_count()
        self.sentence_count = self.sentence_count()
        self.avg_word_per_sentence = self.avg_word_per_sentence()
        self.syllable_count = self.syllable_count()    
        self.avg_syllables_per_word = self.avg_syllables_per_word()


        return self
        
    def setidiom(strIdiom):
        self.idiom=strIdiom


    def summary(self):

        print ('1. Descriptive')
        print ('  Word count=%i' %self.word_count)
        print ('  Sentence count=%i' %self.sentence_count)
        print ('  Syllable count=%i' % self.syllable_count)
        print ('  Avg word per sentence=%f'%self.avg_word_per_sentence)
        print ('  Avg syllable per word=%f' % self.avg_syllables_per_word)
        print ('2. Word Information')
        print ('  Adjective incidence=%f' % self.adjectiveIncidence())
        print ('  Noun incidence=%f' % self.nounIncidence())
        print ('  Verb incidence=%f' % self.verbIncidence())

        print ('3. Syntactic Pattern Density')
        print ('  Content density=%f' % self.contentDensity())

        print ('4. Redability')
        print ('  min(flesch_kincaid, coleman_liau)= %f' % redability.redability(self))
        print ('  Ambiquity=%f' % redability.calcAmbiquity(self))

        print ('5. Connectives')
        print ('  Connectives incidence=%f' % self.adjectiveIncidence())
        print ('  Positive Connectives incidence=%f' % self.adjectiveIncidence())
        print ('  Negative Connectives incidence=%f' % self.adjectiveIncidence())

        print (self.postag)



    #################################
    #### DESCRIPTIVE METRICIS #######
    ########################## ######

    def avg_word_per_sentence (self):
        x=0
        try:
            x= self.word_count / self.sentence_count
        except:
            x=0
        return x
                    
    def avg_syllables_per_word (self):
        x=0
        try:
            x= self.word_count / self.syllable_count
        except:
            x=0
        return x

    def word_count (self):
        if (self.tokens == []):
            self.tokens = tools.getTokens(self.text)
        return len(self.tokens)

    def sentence_count (self):
        x=0
        try:
            tokenized_sentences = nltk.sent_tokenize(self.text)
            x= len(tokenized_sentences)
        except:
            x=0
        return x

    def syllable_count (self):
        x=0
        try:
            count = 0
            vowels = 'aeiouy'
            text = self.text.lower().strip(".:;?!)(")
            if text is not None and text != "":
                if text[0] in vowels:
                    count += 1
                for index in range(1, len(text)):
                    if text[index] in vowels and text[index-1] not in vowels:
                        count += 1
                if text.endswith('e'):
                    count -= 1
                if text.endswith('le'):
                    count += 1
                if count == 0:
                    count += 1
                count = count - (0.1*count)
            x= (round(count))
        except:
            x=0
        return x

   











    ###################################
    #### WORD INFORMATION #############
    ###################################

    def adjectiveIncidence(self):
        if (self.postag == []):
            self.postag = tools.getPosTag(self.tokens)
        
        
        nAdjective=0

        for tag in self.postag:
            word = tag[0]
            word_clas = tag[1]
            if word_clas == "JJ" or word_clas == "JJR" or word_clas == "JJS" :
                nAdjective +=1

        adjectiveIncidence=0
        adjectiveIncidence = nAdjective / float(len(self.postag))*1000
        return adjectiveIncidence


    def nounIncidence(self):
        if (self.postag == []):
            self.postag= tools.getPosTag(self.tokens)
        
        nNoun=0
        for tag in self.postag:
            word = tag[0]
            word_clas = tag[1]
            if word_clas == "NN" or word_clas == "NNS" or word_clas == "NNP" or word_clas == "NNPS" :
                nNoun +=1
        #print('adjective %i' %nAdjective)
        noumIncidence=0

        noumIncidence = nNoun / float(len(self.postag))*1000
        return noumIncidence



    def verbIncidence(self):
        if (self.postag == []):
            self.postag= tools.getPosTag(self.tokens)
        
        nVerb=0
        for tag in self.postag:
            word = tag[0]
            word_clas = tag[1]
            if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
                nVerb +=1
        #print('adjective %i' %nAdjective)
        verbIncidence=0

        verbIncidence = nVerb / float(len(self.postag))*1000
        return verbIncidence




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

    




