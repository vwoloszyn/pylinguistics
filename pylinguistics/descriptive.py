#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from . import tools
import numpy as np


#################################
#### DESCRIPTIVE METRICIS #######
########################## ######

def avg_word_per_sentence(pylinguistObj):
    x = 0
    try:
        x = pylinguistObj.word_count / float(pylinguistObj.sentence_count)
    except:
        x = 0
    pylinguistObj.avg_word_per_sentence = x
    return float(x)


def avg_syllables_per_word(pylinguistObj):
    x = 0
    try:
        x = float(pylinguistObj.syllable_count) / pylinguistObj.word_count
    except:
        x = 0
    pylinguistObj.avg_syllables_per_word = x
    return x


def word_count(pylinguistObj):
    if (pylinguistObj.tokens == []):
        pylinguistObj.tokens = tools.getTokens(pylinguistObj.text)
    count = len(pylinguistObj.tokens)

    for tag in pylinguistObj.postag:
        word = tag[0]
        word_clas = tag[1]
        # punctuations are not words
        if word_clas == ".":
            count -= 1
        # print word

    pylinguistObj.word_count = count
    return count


def orthographic_neighborhood(pylinguistObj):
    if (pylinguistObj.tokens == []):
        pylinguistObj.tokens = tools.getTokens(pylinguistObj.text)

    array = []
    for tag in pylinguistObj.postag:
        word = tag[0]
        word_clas = tag[1]
        # punctuations are not words
        if word_clas == ".":
            array
        else:
            array.append(word)

    count = 0
    for index in range(len(array)):
        for x in range(1, 20):
            if ((index + x) < len(array)):
                if (array[index] == array[index + x]):
                    count = count + 1

    print(count)
    return count


def tokenized_sentences(pylinguistObj):
    try:
        if (pylinguistObj.language == "pt-br"):
            nltk.sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
            tokenized_sentences = nltk.sent_tokenizer.tokenize(pylinguistObj.text)
        else:
            tokenized_sentences = nltk.sent_tokenize(pylinguistObj.text)

    except ValueError:
        print('error:' + ValueError)

    return tokenized_sentences


def sentence_count(pylinguistObj):
    x = len(pylinguistObj.tokenized_sentences)

    pylinguistObj.sentence_count = x

    return x


def sentence_sized_30(pylinguistObj):
    temp = pylinguistObj
    # pylinguistObj.tokens = tools.getTokens(value)
    count = 0
    for key, value in enumerate(pylinguistObj.tokenized_sentences):
        temp.text = value
        # print value
        tokens = tools.getTokens(temp)
        if len(tokens) > 30:
            count = count + 1
        total = (key + 1)

    percent = (count * 100) / total
    return percent


def sentence_length(pylinguistObj):
    temp = pylinguistObj
    # pylinguistObj.tokens = tools.getTokens(value)

    array = []
    for key, value in enumerate(pylinguistObj.tokenized_sentences):
        temp.text = value
        tokens = tools.getTokens(temp)
        array.append(len(tokens))

    # returns an int array containing the size of all sentences
    return array


def mean_sentence_length(pylinguistObj):
    array = []
    array = sentence_length(pylinguistObj)

    a = np.array(array)

    return np.mean(a)


def median_sentence_length(pylinguistObj):
    array = []
    array = sentence_length(pylinguistObj)

    a = np.array(array)

    return np.median(a)


def percentile_25_sentence_length(pylinguistObj):
    array = []
    array = sentence_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 25)


def percentile_50_sentence_length(pylinguistObj):
    array = []
    array = sentence_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 50)


def percentile_75_sentence_length(pylinguistObj):
    array = []
    array = sentence_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 75)


def percentile_90_sentence_length(pylinguistObj):
    array = []
    array = sentence_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 90)


def syllable_counter_english(text):
    count = 0
    vowels = 'aeiouy'
    text = text.lower().strip(".:;?!)(")
    if text[0] in vowels:
        count += 1
    for index in range(1, len(text)):
        if text[index] in vowels and text[index - 1] not in vowels:
            count += 1
    if text.endswith('e'):
        count -= 1
    if text.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    count = count - (0.1 * count)
    return (round(count))


def word_length(pylinguistObj):
    if (pylinguistObj.language == "pt"):
        # from source.syllable import silva2011
        # import source.syllable.silva2011
        from .resources.syllable.silva2011 import syllable_separator

        array = []
        count_error = 0
        for w in pylinguistObj.tokens:
            count = 0

            w = tools.clear_string(w.encode('utf-8'))
            if len(w) > 1:
                # print ('separando palavra:%s' %w_clean)
                try:
                    syllables = syllable_separator.separate(w)
                    leng = len(syllables)
                    count += leng
                # print ('word:%s syllables:%s %i ' %(w, syllables,leng))
                except:
                    count_error += 1
                # print ('ERROR ON WORD: %s' %w)
            array.append(count)

        # pylinguistObj.word_length = array 			#Not working
        return array
    else:
        # print "ELSE"
        array = []
        count_error = 0
        for w in pylinguistObj.tokens:
            count = 0
            # w_clean = tools.clear_string(w)
            w = tools.clear_string(w.encode('utf-8'))
            if len(w) > 1:
                # result =
                # print ('separando palavra:%s' %w_clean)
                try:
                    leng = syllable_counter_english(w)
                    count += leng
                # print ('word:%s syllables:%i ' %(w,leng))
                except:
                    count_error += 1
                # print ('ERROR ON WORD: %s' %w)
            array.append(count)

        return array
    # Syllable counting needs fixing
    # print array


def mean_word_length(pylinguistObj):
    array = []
    array = word_length(pylinguistObj)

    a = np.array(array)

    return np.mean(a)


def median_word_length(pylinguistObj):
    array = []
    array = word_length(pylinguistObj)

    a = np.array(array)

    return np.median(a)


def percentile_25_word_length(pylinguistObj):
    array = []
    array = word_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 25)


def percentile_50_word_length(pylinguistObj):
    array = []
    array = word_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 50)


def percentile_75_word_length(pylinguistObj):
    array = []
    array = word_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 75)


def percentile_90_word_length(pylinguistObj):
    array = []
    array = word_length(pylinguistObj)

    a = np.array(array)

    return np.percentile(a, 90)


def syllable_count(pylinguistObj):
    x = 0
    if (pylinguistObj.language == "pt"):
        # from source.syllable import silva2011
        # import source.syllable.silva2011
        from .resources.syllable.silva2011 import syllable_separator
        count = 0
        count_error = 0
        for w in pylinguistObj.tokens:
            w_clean = tools.clear_string(w)
            w = tools.clear_string(w.encode('utf-8'))
            if len(w) > 1:
                # result =
                # print ('separando palavra:%s' %w_clean)
                try:
                    syllables = syllable_separator.separate(w)
                    leng = len(syllables)
                    count += leng
                # print ('word:%s syllables:%s %i ' %(w, syllables,leng))
                except:
                    count_error += 1
                # print ('ERROR ON WORD: %s' %w)

        pylinguistObj.syllable_count = count
        return count
    else:
        # print "ELSE"
        count = 0
        count_error = 0
        for w in pylinguistObj.tokens:
            # w_clean = tools.clear_string(w)
            w = tools.clear_string(w.encode('utf-8'))
            if len(w) > 1:
                # result =
                # print ('separando palavra:%s' %w_clean)
                try:
                    leng = syllable_counter_english(w)
                    count += leng
                # print ('word:%s syllables:%i ' %(w,leng))
                except:
                    count_error += 1
                # print ('ERROR ON WORD: %s' %w)

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
