from . import tools

###################################
##### Syntactic Pattern Density ###
###################################

# VERB - verbs (all tenses and modes)
# NOUN - nouns (common and proper)
# PRON - pronouns
# ADJ - adjectives
# ADV - adverbs
# ADP - adpositions (prepositions and postpositions)
# CONJ - conjunctions
# DET - determiners
# NUM - cardinal numbers
# PRT - particles or other function words
# X - other: foreign words, typos, abbreviations
# . - punctuation

def contentDensity(pylinguistObj):
    if (pylinguistObj.postag == []):
        pylinguistObj.postag= tools.getPosTag(pylinguistObj)
    
    nVerb=0
    nNoun=0
    nAdjective=0
    nAdverb=0
    
    for tag in pylinguistObj.postag:
        word = tag[0]
        word_clas = tag[1]
        #if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
        if word_clas == "VERB" :
            nVerb +=1
        #elif word_clas == "NN" or word_clas == "NNS" or word_clas == "NNP" or word_clas == "NNPS" :
        elif word_clas == "NOUN"  :
            nNoun +=1
        #elif word_clas == "JJ" or word_clas == "JJR" or word_clas == "JJS" :
        elif word_clas == "ADJ" :
            nAdjective +=1
        #elif word_clas == "RB" or word_clas == "RBR" or word_clas == "RBS":
        elif word_clas == "ADV" :
            nAdverb +=1
    
    contentDensity=10
    #print ('somatorio %i'%(nVerb+nNoun+nAdjective+nAdverb))
    #print ('dividido por %i'%len(postag))

    content_words = nVerb+nNoun+nAdjective+nAdverb
    function_words = float(len(pylinguistObj.postag)-content_words)
    
    content_density = content_words / function_words if function_words else 0
        
    return content_density
