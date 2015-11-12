import nltk
#import sys
#sys.path.append("./resc/nlpnet")
#import nlpnet

from nltk.tag.perceptron import PerceptronTagger
tagger = PerceptronTagger()


from nltk.tokenize import sent_tokenize

def getTokens(text):
	try:
		#if (text.strip() !=""):
		return nltk.word_tokenize(text)
	except:
		return [] 

    #check lenght words
    #tokens = [w.lower() for w in tokens if len(w)<20]


def getPosTag(pylinguistObj):

	#if (idiom == "en"): 
	#optimization
	try:
		#if (len(pylinguistObj.tokens)>0):
		return nltk.tag._pos_tag(pylinguistObj.tokens, None, tagger)
	except:
		return []
	#return nltk.pos_tag(pylinguistObj.tokens)
	#else:


