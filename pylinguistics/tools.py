#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import nltk.tag
from nltk.tag.perceptron import PerceptronTagger
from nltk.tokenize import sent_tokenize
import re
import os,sys
import shlex

tagger = None

def load_tagger(language):
	print('LOAD TAGGER....')
	global tagger
	if (language=="en"):
		tagger = PerceptronTagger()
	elif (language=="pt-br"):
		print('tagger pt-br')


		import nlpnet
		path = os.path.dirname(__file__) + '/resources/pos-pt/'
		#print ('ciretori: %s' %path)
		tagger = nlpnet.POSTagger(path, language='pt')

		"""
		tagger = PerceptronTagger(load=False)
		try:
			print('Loading portuguese.pickle')
			tagger.load('portuguese_tags.pickle')

			
		except:
			print('Error on loading portuguese.pickle')
			import nltk.corpus
			import ast, sys

			print('Creating new tagger model')
			import nltk.corpus

			tsents = nltk.corpus.mac_morpho.tagged_sents()[:1100000]
			#tsents = nltk.corpus.floresta.tagged_sents()

			#sentences = [[(clear_string(w.encode('ascii','ignore')).lower(), t.upper()) for (w,t) in sent if w.encode('ascii','ignore').strip() != ""] for sent in tsents if sent]
			#sentences = [[(w.lower(), t.upper()) for (w,t) in sent if ( w.strip() != "" and t.strip() != "") ] for sent in tsents if sent]
			sentences = [[(w.lower(),t.upper()) for (w,t) in sent] for sent in tsents if sent]
			print ('Corpus lenght:%i' %len(tsents))

			train = sentences[int(len(sentences)*0.7):]
			test = sentences[:int(len(sentences)*0.3)]

			#train = sentences[90000:]
			#test = sentences[:10000]

			#tagger0 = nltk.DefaultTagger('n')
			#tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
			#tagger2 = nltk.BigramTagger(train, backoff=tagger1)
			#evaluate=tagger2.evaluate(test)
			
			
			tagger.train(train, 'portuguese_tags.pickle')
			evaluate=tagger.evaluate(test)

			print('Model accuracy:%f' %evaluate)


		"""




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
			#sys.exit(0)
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
	if (pylinguistObj.language == "pt-br"):
		sents =tagger.tag(pylinguistObj.text.lower())
		#print(sent)
		tags=[]
		tokens=[]
		idx=0
		for sent in sents:
			for t in sent:
				tags.append((t[0],str(t[1])))
				tokens.append(t[0])
				idx+=1
		pylinguistObj.tokens=tokens

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
	dic ={"PREP|+":"ADP","ADJ":"ADJ","ADV":"ADV","ADV-KS":"ADV-KS","ART":"DET","ADV-KS-REL":"ADV","KC":"CONJ","KS":"CONJ","IN":"IN","N":"NOUN",\
		"NPROP":"NOUN","NUM":"NUM","PCP":"PRT","PDEN":"X","PREP":"ADP","PROADJ":"PRON","PRO-KS":"PRO-KS","PROPESS":"PRON","PRO-KS-REL":"PRO-KS-REL",\
		"PROSUB":"PRON","V":"VERB","VAUX":"VERB","CUR":"X","|EST":"X","|AP":"X","|DAD":"X","PREP+ART":"ADP","PREP+PROPESS":"ADP","PREP+ADV":"ADP",\
		"PREP+PROADJ":"ADP","PREP+PRO-KS-REL":"ADP","PREP+PROSUB":"ADP","PU":".","-":".",",":".","N|DAT":"NUM","PREP|+":"ADP"}

	newtag = []
	for c in tags:
		newtag.append((c[0], dic.get(str(c[1]),str(c[1]))))

	fixedtag = []
	aux = "."

	for c in newtag:
		aux = c[1]
		word = c[0].encode('utf-8')
		if word == "“" or word == "’" or word == "‘" or word == "”":
			aux = "."
		fixedtag.append((c[0], aux))

	return fixedtag
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
