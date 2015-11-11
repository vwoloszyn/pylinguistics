# Fibonacci numbers module



import tools
import redability
import descriptive
import wordInformation
import disfluencies



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

       
        #Descriptive counts       
        self.word_count = descriptive.word_count(self)
        self.sentence_count = descriptive.sentence_count(self)
        self.avg_word_per_sentence = descriptive.avg_word_per_sentence(self)
        #self.syllable_count = descriptive.syllable_count(self)    
        #self.avg_syllables_per_word = descriptive.avg_syllables_per_word(self)

        return self
                
    def setLanguage(strLanguage):
        self.language=strLanguage



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






    ###METRICS

    ###########################
    ### Word Information ######
    ###########################

    def adjectiveIncidence(self):
        return wordInformation.adjectiveIncidence(self)

    def nounIncidence(self):
        return wordInformation.nounIncidence(self)

    def verbIncidence(self):
        return wordInformation.verbIncidence(self)


    #Pronoun incidence
    #Age of acquisition for content words, mean
    #Familiarity for content words, mean
    #Concreteness for content words, mean
    #magability for content words, mean
    #Meaningfulness, Colorado norms, content words, mean
    #Polysemy for content words, mean
    #Hypernymy for nouns, mean
    #Hypernymy for verbs, mean
    #Hypernymy for nouns and verbs, mean



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
    













