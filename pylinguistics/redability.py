import nltk
import tools
from nltk.corpus import wordnet as wn


 ###################################
#### REDABILITY ###################
###################################

def redability(pylinguistObj): 
    return min(calc_flesch_kincaid_grade(pylinguistObj), calc_coleman_liau_index(pylinguistObj))

def calc_coleman_liau_index (pylinguistObj):
    texto = pylinguistObj.text.decode('utf-8','ignore')
    x=0
    try:
        x= textstat.coleman_liau_index(texto)
    except:
        x=0
    return x

def calc_flesch_kincaid_grade (pylinguistObj):
    texto = pylinguistObj.text.decode('utf-8','ignore')
    x=0
    try:
        ASL = textstat.avg_sentence_length(texto)
        ASW = textstat.avg_syllables_per_word(texto)
        FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
        x= round(FKRA, 1)
    except:
        x=0
    return x


def calcAmbiquity(pylinguistObj):
    if (pylinguistObj.postag == []):
        pylinguistObj.postag= tools.getPosTag(pylinguistObj)


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

    for tag in pylinguistObj.postag:
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

