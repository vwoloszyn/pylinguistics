#!/usr/bin/python
# -*- coding: utf-8 -*-


from pylinguistics import tools
from pylinguistics import redability
from pylinguistics import descriptive
from pylinguistics import wordInformation
from pylinguistics import disfluencies
from pylinguistics import logic_operators
from pylinguistics import connectives


def text(text, lang='pt-br'):
    # print(text)
    pl = pylinguistics()
    pl.language = lang
    return pl.text(text)


class pylinguistics:

    def __init__(self):
        self.language = "pt-br"
        # text(self, text)
        self.tokens = []
        self.types = []
        self.postag = []

        # return None

    def from_pos_tag(self, postag):
        for word, tag in tagged_text:
            self.tokens.append(word)
        self.postag = postag

    def text(self, text):
        self.types = []
        self.tokens = []
        self.postag = []

        self.text = text
        # .decode('utf-8','ignore')
        self.tokens = tools.getTokens(self)

        # optimization
        self.postag = tools.getPosTag(self)

        # Descriptive counts
        self.tokenized_sentences = descriptive.tokenized_sentences(self)
        self.word_count = descriptive.word_count(self)
        self.sentence_count = descriptive.sentence_count(self)
        self.avg_word_per_sentence = descriptive.avg_word_per_sentence(self)
        # self.word_length = descriptive.word_length(self)                       #Doesn't work, for some reason
        # self.syllable_count = descriptive.syllable_count(self)
        # self.avg_syllables_per_word = descriptive.avg_syllables_per_word(self)

        return self

    def setLanguage(self, strLanguage):
        self.language = strLanguage
        if self.language != "pt" and self.language != "en":
            self.language = "pt"
        print("language: %s" % self.language)

    def getFeatures(self):

        features = {}

        features['word_count'] = descriptive.word_count(self)
        features['sentence_count'] = descriptive.sentence_count(self)
        features['avg_word_per_sentence'] = descriptive.avg_word_per_sentence(self)
        features['syllable_count'] = descriptive.syllable_count(self)
        if self.word_count != 0:
            features['avg_syllables_per_word'] = descriptive.avg_syllables_per_word(self)

        features['sentence_sized_30'] = descriptive.sentence_sized_30(self)
        features['mean_sentence_length'] = descriptive.mean_sentence_length(self)
        features['median_sentence_length'] = descriptive.median_sentence_length(self)
        features['percentile_25_sentence_length'] = descriptive.percentile_25_sentence_length(self)
        features['percentile_50_sentence_length'] = descriptive.percentile_50_sentence_length(self)
        features['percentile_75_sentence_length'] = descriptive.percentile_75_sentence_length(self)
        features['percentile_90_sentence_length'] = descriptive.percentile_90_sentence_length(self)
        if self.word_count != 0:
            features['mean_word_length'] = descriptive.mean_word_length(self)
            features['median_word_length'] = descriptive.median_sentence_length(self)
            features['percentile_25_word_length'] = descriptive.percentile_25_word_length(self)
            features['percentile_50_word_length'] = descriptive.percentile_50_word_length(self)
            features['percentile_75_word_length'] = descriptive.percentile_75_word_length(self)
            features['percentile_90_word_length'] = descriptive.percentile_90_word_length(self)
            # features['orthographic_neighborhood'] = descriptive.orthographic_neighborhood(self)

        # features['word_length'] = descriptive.word_length(self)
        # features['sentence_length'] = descriptive.sentence_length(self)

        features['adjectiveIncidence'] = wordInformation.adjectiveIncidence(self)
        features['nounIncidence'] = wordInformation.nounIncidence(self)
        features['verbIncidence'] = wordInformation.verbIncidence(self)
        features['advIncidence'] = wordInformation.advIncidence(self)
        features['pronIncidence'] = wordInformation.pronIncidence(self)
        features['contentIncidence'] = wordInformation.contentIncidence(self)
        features['functionalIncidence'] = wordInformation.functionalIncidence(self)
        features['LexicalDiversty'] = wordInformation.typeTokensRatio(self)
        features['ContentDiversty'] = wordInformation.contentTokensRatio(self)

        features['adpPronRatio'] = wordInformation.adpPronRatio(self)

        if self.word_count != 0:
            features['LogicNegationIncidence'] = logic_operators.LogicNegationIncidence(self)
            features['LogicIfIncidence'] = logic_operators.LogicIfIncidence(self)
            features['LogicOrIncidence'] = logic_operators.LogicOrIncidence(self)
            features['LogicAndIncidence'] = logic_operators.LogicAndIncidence(self)
            features['LogicOperatorsIncidence'] = logic_operators.LogicOperatorsIncidence(self)

            features['ConnectiveIncidence'] = connectives.ConnectiveIncidence(self)
            features['ConnectiveAdditiveIncidence'] = connectives.AdditiveIncidence(self)
            features['ConnectiveLogicIncidence'] = connectives.LogicIncidence(self)
            features['ConnectiveTemporalIncidence'] = connectives.TemporalIncidence(self)
            features['ConnectiveCasualIncidence'] = connectives.CasualIncidence(self)

            # features['contentDensity'] = self.contentDensity()
            features['redability'] = redability.calc_redability(self)

        return features
