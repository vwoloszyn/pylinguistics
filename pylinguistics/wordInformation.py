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
		adjectiveIncidence = nAdjective / float(len(pylinguistObj.postag))*1000
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
		noumIncidence = nNoun / float(len(pylinguistObj.postag))*1000
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
		verbIncidence = nVerb / float(len(pylinguistObj.postag))*1000
	except:
		verbIncidence = 0
	
	return verbIncidence

