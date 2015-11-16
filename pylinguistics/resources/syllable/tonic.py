#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

# tonic.py - Tonic vowel finding using the algorithm described in Silva [2011].
# Copyright (C) 2014  Alessandro Bokan
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:  Alessandro Bokan <alessandro.bokan@gmail.com>

import re
import codecs
from sys import argv


def tonic_vowel(word):
    """Implements the tonic vowel finding algorithm presented in
    the third chapther of the PhD thesis:

        Silva, D.C. (2011) Algoritmos de Processamento da Linguagem e Síntese
        de Voz com Emoções Aplicados a um Conversor Text-Fala Baseado
        em HMM. PhD dissertation, COPPE, UFRJ.
    """
    # Regra 1: Se existe acento, a vogal marcada é tônica
    match = re.search('á|é|í|ó|ú|â|ê|ô|à|ã|õ', word, re.UNICODE)
    if match:
        return match.start()

    # TODO PALAVRA MARIOR A 2

    # Rule 2: if ^(0) = {r,l,z,x,n} then T = 1
    if re.search('[rlzxn]$', word, re.UNICODE):
        return len(word) - 2

    # Rule 3:
    # if ^(0) = {m} & ^(1) = {i,o,u} then T = 1
    if re.search('[iou]m$', word, re.UNICODE):
        return len(word) - 2

    # Rule 4:
    # if ^(0) = {s} & ^(1) = {n} & ^(2) = {i,o,u} then T = 1
    if re.search('[iou]ns$', word, re.UNICODE):
        return len(word) - 3

    # Rule 5:
    # if ^(0) = {i} & ^(1) = {u,ü} & ^(2) = {q,g} then T = 0
    if re.search('[qg][uü]i$', word, re.UNICODE):
        return len(word) - 1

    # Rule 6:
    # if ^(0) = {s} & ^(1) = {i} & ^(2) = {u,ü} & ^(3) = {q,g} then T = 1
    if re.search('[qg][uü]is$', word, re.UNICODE):
        return len(word) - 2

    # Rule 7:
    # if ^(0) = {i,u} & ^(1) = {a,e,i,o,u} then T = 1
    if re.search('[aeiou][iu]$', word, re.UNICODE):
        return len(word) - 2
    # if ^(0) = {i,u} & ^(1) != {a,e,i,o,u} then T = 0
    if re.search('[^aeiou][iu]$', word, re.UNICODE):
        return len(word) - 1

    # Rule 8:
    # if ^(0) = {s} & ^(1) = {i,u} & ^(2) = {a,e,i,o,u} then T = 2
    if re.search('[aeiou][iu]s$', word, re.UNICODE):
        return len(word) - 3

    # Rule 9:
    # if ^(0) = {s} & ^(1) = {i,u} & ^(2) != {a,e,i,o,u} then T = 2
    if re.search('[^aeiou][iu]s$', word, re.UNICODE):
        return len(word) - 2

    # Rule 10:
    # if ^(0) = {e} & ^(1) = {u} & ^(2) = {q} & ^(3) = {r} & ^(4) = {o} &
    # ^(4) = {p} then T = 0
    if word == "porque":
        return len(word) - 1

    # Rule 11
    # if ^(0) = {e} & ^(1) = {u} & ^(2) = {qg} & ^(3) = {a,e,i,o,u} then T = 3
    if re.search('[aeiou][qg]ue$', word, re.UNICODE):
        return len(word) - 4
    # if ^(0) = {e} & ^(1) = {u} & ^(2) = {qg} & ^(3) != {a,e,i,o,u} then T = 4
    if re.search('[^aeiou][qg]ue$', word, re.UNICODE):
        return len(word) - 5

    # Rule 12
    # if ^(0)={e} & ^(1)={e} & ^(2)={u} & ^(3)={qg} & ^(4)={aeiou} then T = 4
    if re.search('[aeiou][qg]ues$', word, re.UNICODE):
        return len(word) - 5
    # if ^(0)={e} & ^(1)={e} & ^(2)={u} & ^(3)={qg} & ^(4)!={aeiou} then T = 5
    if re.search('[^aeiou][qg]ues$', word, re.UNICODE):
        return len(word) - 6

    # Rule 13:
    # if ^(0) = {a,e,i,o,u} & ^(2) = {i,u} & ^(3) = {a,e,i,o,u} then T = 2
    if re.search('[aeiou][iu][aeiou]$', word, re.UNICODE):
        return len(word) - 3

    # Rule 14:
    # if ^(0) & ^(3) = {a,e,i,o,u} & ^(2) = {i,u} & ^(1) != {a,e,i,o,u} &
    # ^(4) != {q,g} then T = 3
    if re.search('[^qg][aeiou][iu][^aeiou][aeiou]$', word, re.UNICODE):
        return len(word) - 4

    # Rule 15:
    # if ^(0) = {s} & ^(1) & ^(4) = {a,e,i,o,u} & ^(3) = {i,u} &
    # ^(2) != {a,e,i,o,u} & ^(5) != {q,g} then T = 4
    if re.search('[^qg][aeiou][iu][^aeiou][aeiou]s$', word, re.UNICODE):
        return len(word) - 5

    # Rule 16:
    # if ^(0) = {a,e,o} & ^(1) = cons & ^(2) = {n} & ^(3) = {i,u} &
    # ^(4) = {a,e,i,o,u} then T = 3
    consts = 'bdfghjklmnñpqrstvxyz'
    if re.search('[aeiou][iu]n[' + consts + '][aeo]$', word, re.UNICODE):
        return len(word) - 4

    # Rule 17:
    matches = [m.start() for m in re.finditer('a|e|i|o|u', word, re.UNICODE)]
    if len(matches) >= 2:
        k = matches[-2]
        v = ['a', 'e', 'i', 'o', 'u']
        if word[k] in ['i', 'u'] and word[k - 1] in v and not word[k + 1] in v:
            if k - 2 < 0:
                return 0
            if not word[k - 2] in ['q', 'g']:
                return k - 1

    # Rule 18:
    # if ^(0) = {m} & ^(1) = {e} & ^(2) = {u} & ^(3) = {q} then T = 1
    if word == "quem":
        return len(word) - 2

    # Rule 19:
    # Penultimate vowel of the word
    matches = [m.start() for m in re.finditer('a|e|i|o|u', word, re.UNICODE)]
    if len(matches) >= 2:
        return matches[-2]

    return -1


def word_format(word, position):
    tonic = word + " -> "
    for i in range(len(word)):
        if i == position:
            tonic = tonic + "[']"
        tonic = tonic + word[i]
    return tonic


def read_file(filename):
    f = codecs.open(filename, mode='r', encoding='utf8')
    output = codecs.open("output", mode='w', encoding='utf8')
    errors = codecs.open("errors", mode='w', encoding='utf8')
    for word in f.readlines():
        word = word.strip().lower()
        # TODO Filtrado de palavras com REGEX
        T = tonic_vowel(word)
        if T >= 0:
            output.write(word_format(word, T) + '\n')
        else:
            errors.write(word + '\n')

    f.close()
    output.close()
    errors.close()


def read_word(word):
    print(word_format(word, tonic_vowel(word.lower())))

if __name__ == '__main__':
    print(argv[1], tonic_vowel(argv[1].lower()))
