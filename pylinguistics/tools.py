import nltk
from nltk.tokenize import sent_tokenize

def getTokens(text): 
    tokens = nltk.word_tokenize(text)



    #check lenght words
    #tokens = [w.lower() for w in tokens if len(w)<20]

    return tokens

def getPosTag(tokens):
	
	##if (idiom == "en"): 
	
	return nltk.pos_tag(tokens)