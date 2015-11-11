def text(text):
    self.number_diff_words = 0 #to be calculated
    #should frequency and top words be included?
    self.text = text
    self.word_count = self.word_count(text)
    self.sentence_count = self.sentence_count(text)
    self.avg_word_per_sentence = self.avg_word_per_sentence()
    self.syllable_count = self.syllable_count(text)    
    self.avg_syllables_per_word = self.avg_syllables_per_word(text)
    
        #dfTwitter.write_csv("/sdf/asdf/asd")
    
    

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
