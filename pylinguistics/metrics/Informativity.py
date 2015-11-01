def contentDensity(self):
        sentence = self.text.decode('utf-8')
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