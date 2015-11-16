#!/usr/bin/python
# -*- coding: utf-8 -*-


import tools

LogicNegation = 0
LogicIf = 0
LogicOr = 0
LogicAnd = 0
LogicAll = 0


def Negation(pylinguistObj):
    #Incidência de Negações. Consideramos como negações: não, nem, nenhum, nenhuma, nada, nunca e jamais.
    if (pylinguistObj.language == "pt-br"):
    	dic = [tools.clear_string('não'),tools.clear_string('nem'),tools.clear_string('nenhum'),tools.clear_string('nenhuma'),tools.clear_string('nada'),\
    	tools.clear_string('nunca'),tools.clear_string('jamais')]
    	count =0
    	for w in pylinguistObj.tokens:
    		if tools.clear_string(w) in dic:
    			count+=1
    global LogicNegation
    LogicNegation = count
    return LogicNegation

def If(pylinguistObj):
	#Incidência do operador lógico SE em um texto (desconsidera quando o SE é um pronome).
	if (pylinguistObj.language == "pt-br"):
		dic=[tools.clear_string('se')]
		count =0
		for w in pylinguistObj.tokens:
			if tools.clear_string(w) in dic:
				count+=1
	global LogicIf
	LogicIf = count
	return LogicIf

def Or(pylinguistObj):
	### Incidência do operador lógico OU: #Incidência do operador lógico SE em um texto (desconsidera quando o SE é um pronome).
	if (pylinguistObj.language == "pt-br"):
		dic = [tools.clear_string('ou')]
		count =0
		for w in pylinguistObj.tokens:
			if tools.clear_string(w) in dic:
				count+=1
	global LogicOr
	LogicOr = count
	return LogicOr

def And(pylinguistObj):
	#Incidência do operador lógico SE em um texto (desconsidera quando o SE é um pronome)
	if (pylinguistObj.language == "pt-br"):
		dic = [tools.clear_string('e')]
		count =0
		for w in pylinguistObj.tokens:
			if tools.clear_string(w) in dic:
				count+=1
	global LogicAnd
	LogicAnd = count
	return LogicAnd

def LogicNegationIncidence(pylinguistObj):
	global LogicNegation
	if (LogicNegation==0):
		LogicNegation = Negation(pylinguistObj)
	return LogicNegation / (float(len(pylinguistObj.postag))/1000)


def LogicIfIncidence(pylinguistObj):
	global LogicIf
	if (LogicIf==0):
		LogicIf = If(pylinguistObj)
	return LogicIf / (float(len(pylinguistObj.postag))/1000)

def LogicOrIncidence(pylinguistObj):
	global LogicOr
	if (LogicOr==0):
		LogicOr = Or(pylinguistObj)
	return LogicOr / (float(len(pylinguistObj.postag))/1000)

def LogicAndIncidence(pylinguistObj):
	global LogicAnd
	if (LogicAnd==0):
		LogicAnd = And(pylinguistObj)
	return LogicAnd / (float(len(pylinguistObj.postag))/1000)



def LogicOperators(pylinguistObj):
	global LogicNegation
	if (LogicNegation==0):
		LogicNegation = Negation(pylinguistObj)
	global LogicIf
	if (LogicIf==0):
		LogicIf = If(pylinguistObj)
	global LogicOr
	if (LogicOr==0):
		LogicOr = Or(pylinguistObj)
	global LogicAnd
	if (LogicAnd==0):
		LogicAnd = And(pylinguistObj)
	
	global LogicAll
	LogicAll = LogicNegation + LogicIf + LogicOr + LogicAnd
	return 	LogicAll


def LogicOperatorsIncidence(pylinguistObj):
	global LogicAll
	if (LogicAll==0):
		LogicAll = LogicOperators(pylinguistObj)
	return LogicAll / (float(len(pylinguistObj.postag))/1000)

