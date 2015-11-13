import nltk
import nltk.tag
from nltk.tag.perceptron import PerceptronTagger
from nltk.tokenize import sent_tokenize



tagger = None

def load_tagger(language):
	global tagger
	if (language=="en"):
		tagger = PerceptronTagger()
	elif (language=="pt-br"):
		print('tagger pt-br')
		tagger = PerceptronTagger(load=False)
		try:
			print('loading portuguese.pickle')
			tagger.load('portuguese_tags.pickle')
			#print(tagger.tag('hoje eu vou comer um sanduiche'.split()))
		except:
		
			import nltk.corpus
			import ast
			#from nltk.corpus import floresta
			import nltk
			nltk.download('mac_morpho')
			nltk.download('floresta')
			
			print('traing portuguese.pickle')
			#train = [[('today','NN'),('is','VBZ'),('good','JJ'),('day','NN')],[('yes','NNS'),('it','PRP'),('beautiful','JJ')]]
			#train=[('Um', '>N+art'), ('revivalismo', 'H+n'), ('refrescante', 'N<+adj'), ('O', '>N+art'), ('7_e_Meio', 'H+prop'), ('\xc3\xa9', 'P+v-fin'), ('um', '>N+art'), ('ex-libris', 'H+n'), ('de', 'H+prp'), ('a', '>N+art')]
			#train = nltk.corpus.mac_morpho.tagged_words()
			#nltk.corpus.mac_morpho.tagged_words()

			tsents = nltk.corpus.floresta.tagged_sents()
			tsents = [[(w.lower(), t.upper()) for (w,t) in sent] for sent in tsents if sent]
			train = tsents
			#[100:]
			#print(train)
			tagger.train(train, 'portuguese_tags.pickle')
			tagger.load('portuguese_tags.pickle')


def getTokens(text):
	try:
		#if (text.strip() !=""):
		return nltk.word_tokenize(text.decode('ascii','ignore'))
	except:
		return [] 

    #check lenght words
    #tokens = [w.lower() for w in tokens if len(w)<20]


def getPosTag(pylinguistObj):


	#try:
	if tagger is None:
		load_tagger(pylinguistObj.language)

	print('tokens')
	#print(getTokens('hoje eu vou comer um sanduiche'))
	print(tagger.tag(getTokens('hoje eu vou comer um sanduiche')))


	print(pylinguistObj.tokens)
	#tags=nltk.tag._pos_tag(pylinguistObj.tokens, None, tagger)

	tags=tagger.tag(pylinguistObj.tokens)
	print(tags)
	return tags
	#except:
	#	print('error on getPosTag')
	#	return []


