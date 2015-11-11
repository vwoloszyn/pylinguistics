import nltk
import tools


#################################
#### DESCRIPTIVE METRICIS #######
########################## ######

def avg_word_per_sentence (pylinguistObj):
	x=0
	try:
		x= pylinguistObj.word_count / pylinguistObj.sentence_count
	except:
		x=0
	return x
            
def avg_syllables_per_word (pylinguistObj):
	x=0
	try:
		x= pylinguistObj.word_count / pylinguistObj.syllable_count
	except:
		x=0
	return x

def word_count (pylinguistObj):
	if (pylinguistObj.tokens == []):
		pylinguistObj.tokens = tools.getTokens(pylinguistObj.text)
	return len(pylinguistObj.tokens)

def sentence_count (pylinguistObj):
	x=0
	try:
		tokenized_sentences = nltk.sent_tokenize(pylinguistObj.text)
		x= len(tokenized_sentences)
	except:
		x=0
	return x

	x=0
	return x

def syllable_count (pylinguistObj):
	x=0
	try:
		count = 0
		vowels = 'aeiouy'
		text = pylinguistObj.text.lower().strip(".:;?!)(")
		if text is not None and text != "":
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
		x= (round(count))
	except:
		x=0
	return x

