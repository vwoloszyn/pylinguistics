#!/usr/bin/python
# -*- coding: utf-8 -*-


from . import tools


def Negation(pylinguistObj):
    # Incidência de Negações. Consideramos como negações: não, nem, nenhum, nenhuma, nada, nunca e jamais.
    if (pylinguistObj.language == "pt-br"):
        dic = ['não', 'nem', 'nenhum', 'nenhuma', 'nada', 'nunca', 'jamais']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    else:
        # dic = ['no not don't doesn't didn't won't wouldn't can't couldn't isn't, aren't, wasn't, weren't haven't, hasn't, hadn't shouldn't cannot']
        dic = ['no', 'not', 'none', 'nothing', 'never']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
	# global LogicNegation
	# LogicNegation = count
    return count


def If(pylinguistObj):
    # Incidência do operador lógico SE em um texto (desconsidera quando o SE é um pronome).
    if (pylinguistObj.language == "pt-br"):
        dic = ['se']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    else:
        dic = ['if']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    # global LogicIf
    # LogicIf = count
    return count


def Or(pylinguistObj):
    ### Incidência do operador lógico OU: #Incidência do operador lógico SE em um texto.
    if (pylinguistObj.language == "pt-br"):
        dic = ['ou']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    else:
        dic = ['or']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    # global LogicOr
    # LogicOr = count
    return count


def And(pylinguistObj):
    # Incidência do operador lógico E em um texto.
    if (pylinguistObj.language == "pt-br"):
        dic = ['e']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    else:
        dic = ['and']
        count = 0
        for w in pylinguistObj.tokens:
            w = w.encode('utf-8').lower()
            if w in dic:
                # print(w)
                count += 1
    # global LogicAnd
    # LogicAnd = count
    # print(count)
    return count


def LogicOperators(pylinguistObj):
    LogicNegation = Negation(pylinguistObj)

    LogicIf = If(pylinguistObj)

    LogicOr = Or(pylinguistObj)

    LogicAnd = And(pylinguistObj)

    LogicAll = LogicNegation + LogicIf + LogicOr + LogicAnd
    return LogicAll


def LogicNegationIncidence(pylinguistObj):
    LogicNegation = Negation(pylinguistObj)
    return LogicNegation / (float(pylinguistObj.word_count) / 1000)


def LogicIfIncidence(pylinguistObj):
    LogicIf = If(pylinguistObj)
    return LogicIf / (float(pylinguistObj.word_count) / 1000)


def LogicOrIncidence(pylinguistObj):
    LogicOr = Or(pylinguistObj)
    return LogicOr / (float(pylinguistObj.word_count) / 1000)


def LogicAndIncidence(pylinguistObj):
    LogicAnd = And(pylinguistObj)
    return LogicAnd / (float(pylinguistObj.word_count) / 1000)


def LogicOperatorsIncidence(pylinguistObj):
    LogicAll = LogicOperators(pylinguistObj)
    return LogicAll / (float(pylinguistObj.word_count) / 1000)

