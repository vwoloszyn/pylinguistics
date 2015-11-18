#!/usr/bin/python
# -*- coding: utf-8 -*-


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




dic_aditive=["modo","entretanto","todavia","do","contudo","entanto","além","disso","demais","ademais","outrossim","ainda","mais","cima","por",\
"outro","lado","também","e","nem","não","só","mas","não","só","como","apenas","bem","como","com","ou","e/ou"]

dic_logic=["e","ou","se","então","somente"]

dic_temp=["tempo","então","enfim","logo","depois","principio", "no", "momento", "pouco", "antes", "depois"\
"anteriormente","posteriormente","em","seguida","final","fim","finalmente","agora","atualmente","hoje","fequentemente"\
"constantemente","às","vezes","eventualmente","vezes","ocasionalmente","sempre","raramente","raro","não","mesmo","tempo"\
"simultanemanete","interim","nesse","meio","hiato","enquanto","quando","antes","depois","logo","sempre","assim","desde","todas"\
"cada","apenas","já","mal","bem","até"]


dic_casual=["consequentemente","que","dado","de","por","consequencia","conseguinte","resultado","isso","por","causa","em","virtude"\
"asim","fato","efeito","tão","porque","porquê","porquanto","pois","já","uma","vez","visto","portanto"\
"logo","tal","sorte","tal","forma","haja","vista"]



def Connectives(pylinguistObj):
	ConnectiveAll = 0
	#print ('conjuncoes: ')
	if (pylinguistObj.language == "pt-br"):
		for (w,t) in pylinguistObj.postag:
			if (t == "CONJ" ):
				#print w
				ConnectiveAll+=1
	return ConnectiveAll


def Additive(pylinguistObj):
	ConnectiveAdditive = 0
	if (pylinguistObj.language == "pt-br"):
		for (w,t) in pylinguistObj.postag:
			w=w.encode('utf-8').lower()
			if (t == "CONJ" and w in dic_aditive):
				#print ('aditive: %s' %w)
				ConnectiveAdditive+=1
	return ConnectiveAdditive


def Logic(pylinguistObj):
	ConnectiveLogic = 0
	if (pylinguistObj.language == "pt-br"):
		for (w,t) in pylinguistObj.postag:
			w=w.encode('utf-8').lower()
			if (t == "CONJ" and w in dic_logic):
				#print ('logic: %s' %w)
				ConnectiveLogic+=1
	return ConnectiveLogic


def Temporal(pylinguistObj):
	ConnectiveTemporal = 0
	if (pylinguistObj.language == "pt-br"):
		for (w,t) in pylinguistObj.postag:
			w=w.encode('utf-8').lower()
			if (t == "CONJ" and w in dic_temp):
				#print ('Temporal: %s' %w)
				ConnectiveTemporal+=1
	return ConnectiveTemporal


def Casual(pylinguistObj):
	ConnectiveCasual = 0
	if (pylinguistObj.language == "pt-br"):
		for (w,t) in pylinguistObj.postag:
			w=w.encode('utf-8').lower()
			if (t == "CONJ" and w in dic_casual):
				#print ('Casual: %s' %w)
				ConnectiveCasual+=1
	return ConnectiveCasual









def ConnectiveIncidence(pylinguistObj):
	ConnectiveAll = Connectives(pylinguistObj)
	return ConnectiveAll / (float(len(pylinguistObj.postag))/1000)


def AdditiveIncidence(pylinguistObj):
	ConnectiveAdditive = Additive(pylinguistObj)
	return ConnectiveAdditive / (float(len(pylinguistObj.postag))/1000)

def LogicIncidence(pylinguistObj):
	ConnectiveLogic = Logic(pylinguistObj)
	return ConnectiveLogic / (float(len(pylinguistObj.postag))/1000)

def TemporalIncidence(pylinguistObj):
	ConnectiveTemporal = Temporal(pylinguistObj)
	return ConnectiveTemporal / (float(len(pylinguistObj.postag))/1000)


def CasualIncidence(pylinguistObj):
	ConnectiveCasual = Casual(pylinguistObj)
	return ConnectiveCasual / (float(len(pylinguistObj.postag))/1000)



