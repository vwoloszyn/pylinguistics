
    def calcAmbiguidadte(self):
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



class Ambiguity(base.Category):
    name = 'Ambiguity'
    table_name = 'ambiguity'

    def __init__(self):
        super(Ambiguity, self).__init__()
        self._set_metrics_from_module(__name__)
        self.metrics.sort(key=lambda m: m.name)