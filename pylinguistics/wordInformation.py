import nltk
import tools


def adjectiveIncidence(pylinguistObj):
	if (pylinguistObj.postag == []):
		pylinguistObj.postag = tools.getPosTag(pylinguistObj)


	nAdjective=0

	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		if word_clas == "JJ" or word_clas == "JJR" or word_clas == "JJS" :
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
		if word_clas == "NN" or word_clas == "NNS" or word_clas == "NNP" or word_clas == "NNPS" :
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
		if word_clas == "VB" or word_clas == "VBD" or word_clas == "VBG" or word_clas == "VBN" or word_clas == "VBP" or word_clas == "VBZ" :
			nVerb +=1
	#print('adjective %i' %nAdjective)
	verbIncidence=0

	try:
		verbIncidence = nVerb / float(len(pylinguistObj.postag))*1000
	except:
		verbIncidence = 0
	
	return verbIncidence

