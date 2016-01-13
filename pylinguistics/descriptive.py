#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import tools


#################################
#### DESCRIPTIVE METRICIS #######
########################## ######

def avg_word_per_sentence (pylinguistObj):
	x=0
	try:
		x= pylinguistObj.word_count / float(pylinguistObj.sentence_count)
	except:
		x=0
	pylinguistObj.avg_word_per_sentence = x
	return float(x)
            
def avg_syllables_per_word (pylinguistObj):
	x=0
	try:
		x=  float(pylinguistObj.syllable_count) / pylinguistObj.word_count
	except:
		x=0
	pylinguistObj.avg_syllables_per_word = x
	return x

def word_count (pylinguistObj):
	if (pylinguistObj.tokens == []):
		pylinguistObj.tokens = tools.getTokens(pylinguistObj.text)
	count = len(pylinguistObj.tokens)

	for tag in pylinguistObj.postag:
		word = tag[0]
		word_clas = tag[1]
		#ponctuations are not words
		if word_clas == "." :
			count -=1
			#print word

	pylinguistObj.word_count = count
	return count

def sentence_count (pylinguistObj):
	x=0
	#adicionando ponto final de linha
	
	pylinguistObj.text = pylinguistObj.text.replace(' \n', '.')
	#print pylinguistObj.text
	try:
		if (pylinguistObj.language == "pt-br"):
			nltk.sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
			tokenized_sentences = nltk.sent_tokenizer.tokenize(pylinguistObj.text)
		else:
			tokenized_sentences = nltk.sent_tokenize(pylinguistObj.text)

		x= len(tokenized_sentences)
	except ValueError:
		#print('error:' +ValueError)
		x=0
	pylinguistObj.sentence_count = x
	return x

	x=0
	return x

def syllable_counter_english(text):
    count = 0
    vowels = 'aeiouy'
    text = text.lower().strip(".:;?!)(")
    if text[0] in vowels:
        count += 1
    for index in range(1, len(text)):
        if text[index] in vowels and text[index-1] not in vowels:
            count += 1
    if text.endswith('e'):
        count -= 1
    if text.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    count = count - (0.1*count)
    return (round(count))

def syllable_count (pylinguistObj):
	x=0
	if (pylinguistObj.language == "pt-br"):
		#from source.syllable import silva2011
		#import source.syllable.silva2011
		from resources.syllable.silva2011 import syllable_separator
		count=0
		count_error=0
		for w in pylinguistObj.tokens:
			#w_clean = tools.clear_string(w)
			w = tools.clear_string(w.encode('utf-8'))
			if len(w)>1:
				#result = 
				#print ('separando palavra:%s' %w_clean)
				try:
					syllables = syllable_separator.separate(w)
					leng = len(syllables)
					count+=leng
					#print ('word:%s syllables:%s %i ' %(w, syllables,leng))
				except:
					count_error+=1
					#print ('ERROR ON WORD: %s' %w)
			
		pylinguistObj.syllable_count = count
		return count
	else:
		count=0
		count_error=0
		for w in pylinguistObj.tokens:
			#w_clean = tools.clear_string(w)
			w = tools.clear_string(w.encode('utf-8'))
			if len(w)>1:
				#result = 
				#print ('separando palavra:%s' %w_clean)
				try:
					leng = syllable_counter_english(w)
					count+=leng
					#print ('word:%s syllables:%i ' %(w,leng))
				except:
					count_error+=1
					#print ('ERROR ON WORD: %s' %w)
			
		pylinguistObj.syllable_count = count
		return count
	# try:

	# 	count = 0
	# 	vowels = 'aeiouy'
	# 	text = pylinguistObj.text.lower().strip(".:;?!)(")
	# 	if text is not None and text != "":
	# 		if text[0] in vowels:
	# 			count += 1
	# 		for index in range(1, len(text)):
	# 			if text[index] in vowels and text[index-1] not in vowels:
	# 				count += 1
	# 		if text.endswith('e'):
	# 			count -= 1
	# 		if text.endswith('le'):
	# 			count += 1
	# 		if count == 0:
	# 			count += 1
	# 		count = count - (0.1*count)
	# 	x= (round(count))
	# except:
	# 	x=0
	# pylinguistObj.syllable_count = x
	return x

