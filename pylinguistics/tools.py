#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import nltk.tag
from nltk.tag.perceptron import PerceptronTagger
from nltk.tokenize import sent_tokenize
import re



tagger = None

def load_tagger(language):
	print('LOAD TAGGER....')
	global tagger
	if (language=="en"):
		tagger = PerceptronTagger()
	elif (language=="pt-br"):
		print('tagger pt-br')
		tagger = PerceptronTagger(load=False)
		try:
			print('loading portuguese.pickle')
			tagger.load('portuguese_tags.pickle')

			
		except:

			import nltk.corpus
			import ast

			print('evaluating')
			import nltk.corpus

			tsents = nltk.corpus.mac_morpho.tagged_sents()
			print ('len:%i' %len(tsents))

			#sentencesClean = [[(clear_string(w.encode('ascii','ignore')).lower(), t.upper()) for (w,t) in sent if w.encode('ascii','ignore').strip() != ""] for sent in tsents if sent]
			#sentences = [[(w.lower(), t.upper()) for (w,t) in sent] for sent in tsents if sent]
			
			sentences = [[(clear_string(w.encode('ascii','ignore')).lower(), t.upper()) for (w,t) in sent if w.encode('ascii','ignore').strip() != ""] for sent in tsents if sent]

			#sentences = [[(w.lower(), t.upper()) for (w,t) in sent if w.encode('ascii','ignore').strip() != ""] for sent in tsents if sent]
			#.decode('ISO 8859-1')
			#print(sentences)
			#print(sentencesClean)
			train = sentences[sentences*0.7:]
			test = sentences[:sentences*0.3]
			tagger.train(train)
			evaluate=tagger.evaluate(test)
			#evaluateClean=tagger.evaluate(sentencesClean)

			print('accuracy:%f' %evaluate)
			#print('precision with clean:%f' %evaluateClean)
			#print(tagger.tag('hoje eu vou comer um sanduiche'.split()))
			sys.exit(0)




			import nltk.corpus
			import ast
			#from nltk.corpus import floresta
			import nltk
			nltk.download('mac_morpho')
			#nltk.download('floresta')
			
			print('training portuguese.pickle')
			#train = [[('today','NN'),('is','VBZ'),('good','JJ'),('day','NN')],[('yes','NNS'),('it','PRP'),('beautiful','JJ')]]
			#train=[('Um', '>N+art'), ('revivalismo', 'H+n'), ('refrescante', 'N<+adj'), ('O', '>N+art'), ('7_e_Meio', 'H+prop'), ('\xc3\xa9', 'P+v-fin'), ('um', '>N+art'), ('ex-libris', 'H+n'), ('de', 'H+prp'), ('a', '>N+art')]
			#train = nltk.corpus.mac_morpho.tagged_words()
			#nltk.corpus.mac_morpho.tagged_words()
			#.decode('utf-8')
			tsents = nltk.corpus.mac_morpho.tagged_sents()
			tsents = [[(clear_string(w.encode('ascii','ignore')).lower(), t.upper()) for (w,t) in sent if w.encode('ascii','ignore').strip() != ""] for sent in tsents if sent]
			train = tsents
			#print train[100:]
			#print(train)
			tagger.train(train, 'portuguese_tags.pickle')
			tagger.load('portuguese_tags.pickle')


def getTypes(pylinguistObj):
	dic_types={}
	types=[]
	for t in pylinguistObj.tokens:
		dic_types[t]=1

	for w in dic_types:
		types.append(w)

	pylinguistObj.types = types
	return types


def getTokens(pylinguistObj):
	#try:
		if (pylinguistObj.language == "pt-br"):
			#Python understands the common character encoding used for Portuguese, ISO 8859-1 (ISO Latin 1).
			#tokens = nltk.word_tokenize(clear_string(pylinguistObj.text.encode('utf-8','ignore').lower().decode('ascii','ignore'))
			tokens = nltk.word_tokenize(pylinguistObj.text.lower())
			#print (tokens)
			return tokens
			#.decode('iso-8859-1')
		else:
			return nltk.word_tokenize(pylinguistObj.text)
	#except:
	#	return [] 

    #check lenght words
    #tokens = [w.lower() for w in tokens if len(w)<20]


def getPosTag(pylinguistObj):


	#try:
	if tagger is None:
		load_tagger(pylinguistObj.language)

	#print('tokens')
	#print(getTokens('hoje eu vou comer um sanduiche'))
	#print(tagger.tag(getTokens('hoje eu vou comer um sanduiche')))


	#print(pylinguistObj.tokens)
	#tags=nltk.tag._pos_tag(pylinguistObj.tokens, None, tagger)
	#print(pylinguistObj.tokens)
	tags=tagger.tag(pylinguistObj.tokens)

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

	#retaging
	#if (pylinguistObj.language=="pt-br"):
	dic ={"PREP|+":"ADP","ADJ":"ADJ","ADV-KS":"ADV","ART":"DET","ADV":"ADV","ADV-KS-REL":"ADV","KC":"CONJ","KS":"CONJ","IN":"X","N":"NOUN",\
		"NPROP":"NOUN","NUM":"NUM","PCP":"PRT","PDEN":"X","PREP":"ADP","PROADJ":"PRON","PRO-KS":"PRON","PROPESS":"PRON","PRO-KS-REL":"PRON",\
		"PROSUB":"PRON","V":"VERB","VAUX":"VERB","CUR":"X","|EST":"X","|AP":"X","|DAD":"X","PREP+ART":"ADP","PREP+PROPESS":"ADP","PREP+ADV":"ADP",\
		"PREP+PROADJ":"ADP","PREP+PRO-KS-REL":"ADP","PREP+PROSUB":"ADP","PU":".","-":".",",":".","N|DAT":"NUM","PREP|+":"ADP"}

	newtag = []
	for c in tags:
		newtag.append((c[0], dic.get(str(c[1]),str(c[1]))))

	#print(newtag)
	return newtag
	#except:
	#	print('error on getPosTag')
	#	return []








def clear_string(value):
	#value=""
	#for c in string:
	#print('c:'+c)
	#replaced+=dic.get(c,c)
	value = re.sub('à', "a", value)
	value = re.sub('é', "e", value)
	value = re.sub('ã', "a", value)
	value = re.sub('%', "Porc", value)
	value = re.sub('ó', "o", value)
	value = re.sub('í', "i", value)
	value = re.sub('ê', "e", value)
	value = re.sub('ç', "c", value)
	value = re.sub('õ', "o", value)
	value = re.sub('ú', "u", value)
	value = re.sub('á', "a", value)
	#value = re.sub('\`', "", value)
	#value = re.sub('\'', "", value)

	return value
