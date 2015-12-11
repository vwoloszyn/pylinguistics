import nltk
import tools

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


    ###########################
    ### Word Information ######
    ###########################


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




def adjectiveIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag = tools.getPosTag(pylinguistObj)


	nAdjective=0

	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "JJ" or word_clas == "JJR" or word_clas == "JJS" :
		if word_clas == "ADJ":
			nAdjective +=1

	adjectiveIncidence=0
	try:
		adjectiveIncidence = nAdjective / (float(pylinguistObj.word_count)/1000)
	except:
		adjectiveIncidence = 0

	return adjectiveIncidence


def nounIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	nNoun=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "NN" or word_clas == "NNS" or word_clas == "NNP" or word_clas == "NNPS" :
		if word_clas == "NOUN" :
			nNoun +=1
	#print('adjective %i' %nAdjective)
	noumIncidence=0
	try:
		noumIncidence = nNoun / (float(pylinguistObj.word_count)/1000)
	except:
		noumIncidence = 0

	return noumIncidence



def verbIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	nVerb=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
		if word_clas == "VERB":
			nVerb +=1
	#print('adjective %i' %nAdjective)
	verbIncidence=0

	try:
		verbIncidence = nVerb / (float(pylinguistObj.word_count)/1000)
	except:
		verbIncidence = 0
	
	return verbIncidence


def advIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	nADV=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
		if word_clas == "ADV" or word_clas == "ADV-KS":
			nADV +=1
	#print('adjective %i' %nAdjective)
	advIncidence=0

	try:
		advIncidence = nADV / (float(pylinguistObj.word_count)/1000)
	except:
		advIncidence = 0
	
	return advIncidence


def pronIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	nPRON=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
		if word_clas == "PRON" or word_clas == "PRO-KS" or word_clas == "PRO-KS-REL":
			nPRON +=1
	#print('adjective %i' %nAdjective)
	pronIncidence=0

	try:
		pronIncidence = nPRON / (float(len(pylinguistObj.postag))/1000)
	except:
		pronIncidence = 0
	
	return pronIncidence


def contentIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	count=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
		if word_clas == "VERB" or word_clas == "NOUN" or word_clas == "ADJ" or word_clas == "ADV" :
			count +=1
	#print('adjective %i' %nAdjective)
	incidence=0

	try:
		incidence = count / (float(pylinguistObj.word_count)/1000)
	except:
		incidence = 0
	
	return incidence

"""
def contentOverlap(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	count=0
	index=0
	for index, tag in enumerate(pylinguistObj.postag):
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
		if word_clas == "VERB" or word_clas == "NOUN" or word_clas == "ADJ" or word_clas == "ADV" :
			count +=1
	#print('adjective %i' %nAdjective)

	incidence=0

	try:
		incidence = count / (float(pylinguistObj.word_count))/1000)
	except:
		incidence = 0
	
	return incidence
"""

def functionalIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag= tools.getPosTag(pylinguistObj)

	count=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
		if word_clas == "DET" or word_clas == "ADP" or word_clas == "PRON" or word_clas == "CONJ" or word_clas == "IN" :
			count +=1
	#print('adjective %i' %nAdjective)
	incidence=0

	try:
		incidence = count / (float(pylinguistObj.word_count)/1000)
	except:
		incidence = 0
	
	return incidence

def typeTokensRatio(pylinguistObj):

	""" old function
	tools.getTypes(pylinguistObj)
	ntypes = len(pylinguistObj.types)
	ntokens = len(pylinguistObj.tokens)
	print('ntypes: %i, ntokens: %i' %(ntypes,ntokens))
	return float(ntypes)/float(ntokens)
	"""

	dic_types={}
	types=[]
	ntypes=0
	total=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		if word_clas != "." :
			total +=1
			dic_types[word]=1

	for w in dic_types:
		types.append(w)

	ntypes = len(types)
	#print('ntypes: %i, ntokens: %i' %(ntypes,total))
	return float(ntypes)/float(total)


def contentTokensRatio(pylinguistObj):

	dic_types={}
	types=[]
	ntypes=0
	total=0
	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		if word_clas == "VERB" or word_clas == "NOUN" or word_clas == "ADJ" or word_clas == "ADV" :
			total +=1
			dic_types[word]=1

	for w in dic_types:
		types.append(w)

	ntypes = len(types)
	#print('ntypes: %i, ntokens: %i' %(ntypes,total))
	return float(ntypes)/float(total)
