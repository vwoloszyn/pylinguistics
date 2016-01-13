#!/usr/bin/python
# -*- coding: utf-8 -*-



import tools
import redability
import descriptive
import wordInformation
import disfluencies
import logic_operators
import connectives


def text(text):
    #print(text)
    pl = pylinguistics()
    return pl.text(text)

class pylinguistics:

    def __init__(self):
        self.language="en"
        self.tokens=[]
        self.types=[]
        self.postag=[]

        #return None


    def from_pos_tag(self, postag):
        for word, tag in tagged_text:
            self.tokens.append(word)
        self.postag=postag

    def text(self, text):
        self.types=[]
        self.tokens=[]
        self.postag=[]

        self.text = text
        #.decode('utf-8','ignore')
        self.tokens = tools.getTokens(self)

        #optimization
        self.postag = tools.getPosTag(self)

       
        #Descriptive counts       
        self.word_count = descriptive.word_count(self)
        self.sentence_count = descriptive.sentence_count(self)
        self.avg_word_per_sentence = descriptive.avg_word_per_sentence(self)
        #self.syllable_count = descriptive.syllable_count(self)    
        #self.avg_syllables_per_word = descriptive.avg_syllables_per_word(self)

        return self
                
    def setLanguage(self, strLanguage):
        self.language=strLanguage
        print("language: %s" %self.language)



    def summary(self):
        print ('1. Descriptive')
        print ('  Word count=%i' %self.word_count)
        print ('  Sentence count=%i' %self.sentence_count)
        #print ('  Syllable count=%i' % self.syllable_count)
        print ('  Avg word per sentence=%f'%self.avg_word_per_sentence)
        #print ('  Avg syllable per word=%f' % self.avg_syllables_per_word)

        print ('2. Word Information')
        print ('  Adjective incidence=%f' % self.adjectiveIncidence())
        print ('  Noun incidence=%f' % self.nounIncidence())
        print ('  Verb incidence=%f' % self.verbIncidence())

        print ('3. Syntactic Pattern Density')
        print ('  Content density=%f' % self.contentDensity())

        print ('4. Redability')
        print ('  min(flesch_kincaid, coleman_liau)= %f' % self.redability())
        print ('  Ambiquity=%f' % self.calcAmbiquity())

        #print (self.postag)




    def getFeatures(self):


        features={}

        features['word_count'] = descriptive.word_count(self)
        features['sentence_count'] = descriptive.sentence_count(self)
        features['avg_word_per_sentence'] = descriptive.avg_word_per_sentence(self)
        features['syllable_count'] = descriptive.syllable_count(self)
        features['avg_syllables_per_word'] = descriptive.avg_syllables_per_word(self)


        features['adjectiveIncidence'] = wordInformation.adjectiveIncidence(self)
        features['nounIncidence'] = wordInformation.nounIncidence(self)
        features['verbIncidence'] = wordInformation.verbIncidence(self)
        features['advIncidence'] = wordInformation.advIncidence(self)
        features['pronIncidence'] = wordInformation.pronIncidence(self)
        features['contentIncidence'] = wordInformation.contentIncidence(self)
        features['functionalIncidence'] = wordInformation.functionalIncidence(self)
        features['LexicalDiversty'] = wordInformation.typeTokensRatio(self)
        features['ContentDiversty'] = wordInformation.contentTokensRatio(self)



        features['LogicNegationIncidence'] = logic_operators.LogicNegationIncidence(self)
        features['LogicIfIncidence'] = logic_operators.LogicIfIncidence(self)
        features['LogicOrIncidence'] = logic_operators.LogicOrIncidence(self)
        features['LogicAndIncidence'] = logic_operators.LogicAndIncidence(self)
        features['LogicOperatorsIncidence'] = logic_operators.LogicOperatorsIncidence(self)

        features['ConnectiveIncidence'] = connectives.ConnectiveIncidence(self)
        features['ConnectiveAdditiveIncidence'] = connectives.AdditiveIncidence(self)
        features['ConnectiveLogicIncidence'] = connectives.LogicIncidence(self)
        features['ConnectiveTemporalIncidence'] = connectives.TemporalIncidence(self)
        features['ConnectiveCasualIncidence'] = connectives.CasualIncidence(self)

        



        #features['contentDensity'] = self.contentDensity()
        features['redability'] = redability.calc_redability(self)

        return features        



    ###METRICS





    ####################################
    ### Syntactic Pattern Density ######
    ####################################

    def contentDensity(self):
        return disfluencies.contentDensity(self)


    #Negation density, incidence
    #Gerund density, incidence
    #Infinitive density, incidence




    ####################################
    ### Connectives ####################
    ####################################

    #All connectives incidence
    #Causal connectives incidence
    #Logical connectives incidence
    #Adversative and contrastive connectives incidence
    #Temporal connectives incidence
    #Additive connectives incidence
    #Positive connectives incidence
    #Negative connectives incidence


    ####################################
    ### Referential Cohesion ###########
    ####################################

    #Noun overlap, adjacent sentences,
    #Argument overlap, adjacent sentences,
    #Noun overlap, all sentences
    #Argument overlap, all sentences
    #Content word overlap, adjacent sentences,
    #Content word overlap, all sentences,


    ####################################
    ### Redability  ####################
    ####################################

    def redability(self):
        return redability.redability(self)

    def calcAmbiquity(self):
        return redability.calcAmbiquity(self)
    
    #correctness














