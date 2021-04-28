#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

# silva2011.py - Syllable separation using the algorithm described in Silva
# [2011].
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
#           Andre Cunha      <andre.lv.cunha@gmail.com> (minor modifications)


from .cases import case1, case2, case3, case4, case5, case6, case7, case8
from .tonic import tonic_vowel
from .api import SyllableSeparator

import re
from sys import argv


# Vowels
V = ['a', 'e', 'o', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'ô', 'à', 'ü']

# Semivowels
G = ['i', 'u']

# Stop consonants
COc = ['ca', 'co', 'cu', 'que', 'qui', 'ga', 'go', 'gu', 'gue', 'gui']
CO = ['p', 't',  'b', 'd', 'c', 'g', 'q'] + COc

# Fricative consonants
CFc = ['ce', 'ci', 'ss', 'ch', 'ge', 'gi']
CF = ['f', 'v', 's', 'ç', 'z', 'j', 'x'] + CFc

# Liquid consonants
CL = ['l', 'r', 'rr']

# Nasal consonants
CN = ['m', 'n']

# Consonants
C = ['lh', 'nh'] + CO + CF + CL + CN


class Silva2011SyllableSeparator(SyllableSeparator):
    """This class implements the syllabic separation algorithm presented in
    the fourth chapther of the PhD thesis:

        Silva, D.C. (2011) Algoritmos de Processamento da Linguagem e Síntese
        de Voz com Emoções Aplicados a um Conversor Text-Fala Baseado
        em HMM. PhD dissertation, COPPE, UFRJ.
    """

    def separate(self, w):
        """Separate the syllables of a word.

        Required arguments:
        w -- the word that will be separated in syllables

        Returns:
        A list of strings, containing each syllable of the word.
        """
        vowels = 'a|e|o|i|u|á|é|í|ó|ú|ã|õ|â|ê|ô|à|ü'
        p = [match.start() for match in re.finditer(vowels, w, re.UNICODE)]
        p0 = 0  # syllable start position
        pVt = tonic_vowel(w)  # tonic vowel position
        k = 0
        c = 0  # Count hyfens

        # Just to pass the Biderman simplified.
        if len(w) == 1:
            return [w]

        while p0 <= (len(w) - 1):
            # Rule 1:
            if p[k] + 1 < len(w)\
                    and w[p0] in V\
                    and not w[p[k]] in ['ã', 'õ']\
                    and w[p[k] + 1] in V\
                    and not w[p[k] + 1] in G:
                # print "RULE 1"
                if p[k] + 3 < len(w)\
                        and w[p[k] + 2] == 's'\
                        and p[k] + 3 == len(w):
                    # print "RULE 1.1"
                    return w
                else:
                    # print "RULE 1.2"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 2:
            elif p[k] + 3 < len(w)\
                    and w[p0] in V\
                    and w[p[k] + 1] in C\
                    and w[p[k] + 2] in C\
                    and w[p[k] + 3] in CO:
                # print "RULE 2"
                w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)

            # Rule 3:
            elif p[k] + 2 < len(w)\
                    and w[p0] in V\
                    and w[p[k] + 1] in G + CN + ['s', 'r', 'l', 'x']\
                    and w[p[k] + 2] in C:
                # TODO Problema "arr".
                # Exemplo: arrendar -> a-rre-dar (N) | ar-ren-dar (Y)
                # print "RULE 3"
                if w[p[k] + 1] == 'i'\
                        and w[p[k] + 2] in CN:  # NOVA REGRA, p.ex: "ainda"
                    # print "RULE 3.0"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                elif not w[p[k] + 2] in ['s', 'h']\
                        and w[p[k] + 1] != w[p[k] + 2]:
                    # print "RULE 3.1"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                elif p[k] + 3 < len(w)\
                        and w[p[k] + 1] in CN\
                        and w[p[k] + 2] == 's'\
                        and not w[p[k] + 3] in V:
                    # print "RULE 3.2"
                    w, p0, k, c, p, pVt = case7(w, p, p0, pVt, k, c)
                elif w[p[k] + 1] == w[p[k] + 2]\
                        or w[p[k] + 2] == 'h':
                    # print "RULE 3.3"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                elif p[k] + 3 < len(w)\
                        and w[p[k] + 2] == 's'\
                        and ((w[p[k] + 3] in C and w[p[k] + 3] != 's')
                             or not w[p[k] + 3] in C + V):
                    # print "RULE 3.4"
                    w, p0, k, c, p, pVt = case7(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 3.5"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)

            # Rule 4:
            elif p[k] + 3 < len(w)\
                    and w[p0] in V\
                    and w[p[k] + 1] in CO + CF + ['g', 'p']\
                    and w[p[k] + 2] in CO + CF + CN + ['ç']\
                    and w[p[k] + 3] in V + G:

                # print "RULE 4"
                # TODO adicionando um G ao w[p[k] + 3], p.ex: ab-di-car
                if w[p[k] + 1] == w[p[k] + 2]:
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                else:
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)

            # Rule 5:
            elif p[k] + 2 < len(w)\
                    and w[p0] in V\
                    and w[p[k] + 1] in C\
                    and w[p[k] + 2] in V + G + CL + ['h']:
                # print "RULE 5"
                w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 6:
            elif p[k] + 3 < len(w)\
                    and w[p0] in V\
                    and w[p[k] + 1] in G\
                    and w[p[k] + 2] == 's'\
                    and w[p[k] + 3] in CO:
                # TODO Regra 6 esta dentro da regra 3
                # print "RULE 6"
                w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)

            # Rule 7:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C + ['u', 'ü', 'q']\
                    and w[p[k] + 1] in C\
                    and w[p[k] + 2] in V:
                # print "RULE 7"
                w, p0, k, c, p, pVt = case3(w, p, p0, pVt, k, c)

            # Rule 8:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in G\
                    and w[p[k] + 2] == 'r'\
                    and w[p[k] + 3] in C:
                # print "RULE 8"
                # if p[k] == pVt:
                #    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)
                # else:
                w, p0, k, c, p, pVt = case3(w, p, p0, pVt, k, c)

            # Rule 9:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in G + CN\
                    and w[p[k] + 2] == 's'\
                    and w[p[k] + 3] in CO:
                # print "RULE 9"
                w, p0, k, c, p, pVt = case7(w, p, p0, pVt, k, c)

            # Rule 10:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C + G\
                    and w[p[k] + 1] in ['i', 'u', 'e', 'o']\
                    and p[k] + 1 != pVt\
                    and w[p[k]] != w[p[k] + 1]\
                    and w[p[k] + 2] in C\
                    and w[p[k] + 3] in C + V\
                    and w[p[k] + 2] != 's':
                # print "RULE 10"
                # a-juizado
                if p[k] == pVt\
                        and w[p[k] + 2] != 'n'\
                        and not w[p[k] + 3] in C:
                    # print "RULE 10.1"
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)
                elif not w[p[k] - 1] in ['q', 'g']\
                        and w[p[k]] == 'u'\
                        and w[p[k] + 1] == 'i'\
                        and w[p[k] + 2] != 'n':
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                elif p[k] != pVt\
                        and w[p[k] + 1] == 'i'\
                        and w[p[k] + 2] != 'n':
                    # print "RULE 10.2"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                elif (w[p[k] + 1] != 'i'
                      and w[p[k] + 2] in CN + ['r']
                      and not w[p[k] + 3] in ['h', w[pVt]])\
                        or (w[p[k]] in ['a', 'e', 'o']
                            and w[p[k] + 1] in ['a', 'e', 'o']
                            and w[p[k] + 2] in CN
                            and not w[p[k] + 3] in ['h', 's']
                            and w[p[k] + 4] in V + C):
                    # print "RULE 10.3"
                    if w[p[k] - 1:p[k] + 1] == "gu"\
                            and w[p[k] + 1] in V\
                            and w[p[k] + 2] in CN:
                        w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)
                    elif w[p[k] - 1:p[k] + 1] == "gu"\
                            and w[p[k] + 1] in V\
                            and w[p[k] + 2] in CL:
                        w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                    else:
                        w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                elif w[p[k]] in G\
                        and w[p[k] + 1] in ['a', 'e', 'o']\
                        and w[p[k] + 2] in CN:
                    # print "RULE 10.4"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 10.5"
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)

            # Rule 11:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in G\
                    and w[p[k] + 2] in V:
                # print "RULE 11"
                w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)

            # Rule 12:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k]] in G\
                    and w[p[k] + 1] in V + ['i']\
                    and w[p[k]] != w[p[k] + 1]\
                    and w[p[k] + 2] in C\
                    and w[p[k] + 3] in V:
                # TODO Agregue un "i" as vogais
                #   porque sino no entra ao exemplo.
                # print "RULE 12"
                if w[p[k] - 1] in ['q', 'g']\
                   and ((w[p[k] + 2] == 'ç'
                         and w[p[k] + 3] in ['ã', 'õ'])
                        or (w[p[k] - 1] == 'q'
                            and w[p[k] + 1] in V)):
                    # print "RULE 12.1"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                elif p[k] + 1 == pVt\
                        or w[p[k] - 1] == 'r' and p[k] + 3 == pVt:
                    # print "RULE 12.2"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 12.3"
                    w, p0, k, c, p, pVt = case8(w, p, p0, pVt, k, c)

            # Rule 13:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and (w[p[k] - 1] in C
                         or (w[p[k] - 1:p[k] + 1]
                             in ['qu', 'qü', 'gu', 'gü']))\
                    and w[p[k] + 1] in V + CL + CN + ['c', 'x']\
                    and w[p[k] + 2] in ['h', 'l', 'r']\
                    and w[p[k] + 3] in V + ['h', 'l', 'r']:
                # TODO Arrumando regra para "guerra" -> gue-rra
                # print "RULE 13"
                if w[p[k] + 1] == w[p[k] + 2]\
                        or w[p[k] + 1] in ['c', 'l']\
                        or w[p[k] + 1:p[k] + 3] == 'nh':
                    # print "RULE 13.1"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 13.2"
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)

            # Rule 14:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in CL + CN + ['i']\
                    and w[p[k] + 2] == 's':
                # print "RULE 14"
                if p[k] + 3 == len(w):
                    p0 = case6(w, p0)
                elif p[k] == pVt or (p[k] + 3 < len(w) and w[p[k] + 3] in V):
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)
                else:
                    w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)

            # Rule 15:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] + 1] in V\
                    and w[p[k] + 2] in V + G\
                    and not w[p[k] - 1:p[k] + 1] in ['qu', 'gu']:
                # print "RULE 15", w[p0]
                if p[k] + 3 < len(w)\
                        and p[k] == pVt\
                        and w[p[k] + 1] in G\
                        and w[p[k] + 3] in C:
                    # print "RULE 15.1"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 15.2"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 16:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k]] != 'u'\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in V\
                    and w[p[k] + 2] in CN:
                # print "RULE 16"
                w, p0, k, c, p, pVt = case3(w, p, p0, pVt, k, c)

            # Rule 17:
            elif p[k] + 1 < len(w)\
                    and p[k] - 2 >= 0\
                    and not w[p0] in V\
                    and w[p[k]] == 'i'\
                    and (w[p[k] - 2] in ['á', 'é', 'í', 'ó', 'ú']
                         or w[p[k] - 3] in ['á', 'é', 'í', 'ó', 'ú'])\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in ['a', 'o']:
                # TODO trocar caso 6 por caso 1.
                # carícia -> ca-rí-cia (N) | ca-rí-ci-a (Y)
                # print "RULE 17"
                w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 18:
            elif p[k] + 1 < len(w)\
                    and not w[p0] in V\
                    and w[p[k]] in ['ã', 'õ']\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in ['e', 'o']:
                # print "RULE 18"
                p0 = case6(w, p0)

            # -------------------- Change rule 19 by 20 --------------------
            # Rule 20:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k] + 1] in V\
                    and w[p[k] + 2] in CN\
                    and w[p[k] + 3] in C:
                # print "RULE 20"
                w, p0, k, c, p, pVt = case7(w, p, p0, pVt, k, c)

            # Rule 19:
            elif p[k] + 1 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and p[k] + 1 == pVt\
                    and not w[p[k] + 1] in ['i', 'u']\
                    and not w[p[k] - 1:p[k] + 1] in ['gu', 'qu']:
                # print "RULE 19"
                if p[k] + 3 == len(w)\
                        and w[p[k] - 1:p[k] + 1] in ['gu', 'qu']\
                        and w[p[k] + 1] in V\
                        and w[p[k] + 2] in C:
                    # print "RULE 19.1"
                    p0 = case6(w, p0)
                elif p[k] + 2 < len(w)\
                        and w[p[k] - 1:p[k] + 1] in ['gu', 'qu']\
                        and w[p[k] + 1] in V\
                        and w[p[k] + 2] in C + G:
                    # print "RULE 19.2"
                    w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 19.3"
                    w, p0, k, c, p, pVt = case3(w, p, p0, pVt, k, c)

            # Rule 21:
            elif p[k] + 3 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] + 1] in CO + ['f', 'v', 'g']\
                    and w[p[k] + 2] in CL + CO\
                    and w[p[k] + 3] in V + G:
                # print "RULE 21"
                if w[p[k] + 1] in ['f', 'p']\
                        and w[p[k] + 2] in ['t', 'ç']:
                    # print "RULE 21.1"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                else:
                    # print "RULE 21.2"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 22:
            elif p[k] + 1 < len(w)\
                    and p[k] - 2 >= 0\
                    and not w[p0] in V\
                    and (w[p[k] - 1] in C
                         or w[p[k] - 1:p[k] + 1] in ['qu', 'gu'])\
                    and w[p[k] + 1] in V\
                    and (p[k] + 2 == len(w)
                         or w[p[k] + 2] in C):
                # print "RULE 22"
                if (w[p[k]] in ['i', 'u', 'í', 'ú', 'é', 'ê']
                    and p[k] == pVt
                    and w[p[k] + 1] != 'u')\
                        or (p[k] + 3 < len(w)
                            and not w[p[k]] in G
                            and w[p[k] + 2] == 's'
                            and not w[p[k] + 3] in C + V):
                    # print "RULE 22.1"
                    w, p0, k, c, p, pVt = case3(w, p, p0, pVt, k, c)
                elif p[k] + 2 == len(w)\
                        and w[p[k]] == 'i'\
                        and p[k] == pVt\
                        and w[p[k] + 1] == 'u':
                    # print "RULE 22.2"
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)
                elif p[k] + 3 < len(w)\
                        and ((w[p[k]] in G
                              and p[k] + 1 != pVt
                              and not w[p[k] + 2] in C + V)
                             or (w[p[k] + 2] == 's'
                                 and not w[p[k] + 3] in C + V)
                             or (p[k] != pVt
                             and p[k] + 1 != pVt
                             and w[p[k] + 2] == 's'
                             and p[k] + 3 == len(w))):
                    # print "RULE 22.3"
                    p0 = case6(w, p0)
                elif p[k] + 3 < len(w)\
                        and w[p[k] - 1:p[k] + 1] in ['qu', 'gu']\
                        and w[p[k] + 2] in C\
                        and w[p[k] + 3] in V + G:
                    # print "RULE 22.4"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                elif p[k] + 2 == len(w)\
                        and w[p[k] - 1:p[k] + 1] in ['qu', 'gu']\
                        and w[p[k] + 1] in V + G:
                    # print "RULE 22.4.5"
                    p0 = case6(w, p0)
                elif p[k] + 3 == len(w)\
                        and w[p[k] + 1] in ['o', 'u']\
                        and p[k] + 1 != pVt\
                        and w[p[k] + 2] == 's':
                    # print "RULE 22.5"
                    w, p0, k, c, p, pVt = case7(w, p, p0, pVt, k, c)
                else:
                    # TODO Trocar case2 por case 1
                    # print "RULE 22.6"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 23:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and (w[p[k] - 1] in C
                         or w[p[k] - 2:p[k] - 1] == "qu")\
                    and w[p[k] + 1] in C\
                    and w[p[k] + 2] in C:
                # print "RULE 23"
                if w[p[k] + 1] == w[p[k] + 2]:
                    # print "RULE 23.1"
                    w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)
                elif w[p[k] + 1] == 's'\
                        and w[p[k] + 2] != 's':
                    # print "RULE 23.2"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)
                elif p[k] + 3 < len(w)\
                        and w[p[k] + 2] == 's'\
                        and w[p[k] + 3] in CO:
                    # print "RULE 23.3"
                    w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)
                else:  # Adicionando ELSE
                    # print "RULE 23.4"
                    w, p0, k, c, p, pVt = case2(w, p, p0, pVt, k, c)

            # Rule 24:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] + 1] in C\
                    and w[p[k] + 2] in G:
                # Regra 24 igual a 23. Arrumar regra, p.ex: di-sen-"teria"
                # print "RULE 24"
                w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 25: Already aplicated

            # Rule 26:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and (w[p[k] - 1] in C
                         or (w[p[k] - 1:p[k] + 1]
                             in ['qu', 'qü', 'gu', 'gü']))\
                    and w[p[k] + 1] in G\
                    and w[p[k] + 2] in CN:
                # Manual: a-mi-gui-nho | Automatic: a-mi-gu-i-nho
                # print "RULE 26"
                w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)

            # Rule 27:
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1] in C\
                    and w[p[k] - 2] in C\
                    and w[p[k] + 1] in G\
                    and w[p[k] + 2] in C:
                # print "RULE 27"
                w, p0, k, c, p, pVt = case1(w, p, p0, pVt, k, c)

            # Rule 28
            elif p[k] + 2 < len(w)\
                    and not w[p0] in V\
                    and w[p[k] - 1:p[k] + 1] in ['qu', 'qü', 'gu', 'gü']\
                    and w[p[k] + 1] in V:
                # print "RULE 28"
                if p[k] + 3 < len(w)\
                        and w[p[k] + 2] in C\
                        and w[p[k] + 3] in C:
                    # print "RULE 28.1"
                    w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)
                elif p[k] + 3 < len(w)\
                        and w[p[k] + 2] in C\
                        and w[p[k] + 3] in V + G:
                    # print "RULE 28.2"
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)
                elif p[k] + 2 < len(w)\
                        and w[p[k] + 2] in V:
                    # print "RULE 28.3"
                    w, p0, k, c, p, pVt = case4(w, p, p0, pVt, k, c)
                elif p[k] + 2 < len(w)\
                        and w[p[k] + 2] in G:
                    # print "RULE 28.4"
                    w, p0, k, c, p, pVt = case5(w, p, p0, pVt, k, c)

            p0 += 1

        return w.split('-')

    def _test(self):
        import codecs
        with codecs.open('./simplified/biderman-UTF-8.txt',
                         encoding='utf-8', mode='r') as content_file,\
            codecs.open('./simplified/biderman_output.txt',
                        encoding='utf-8', mode='w') as output_file:

            content = content_file.read()
            lines = content.split('\n')
            for line in lines:
                word = line.split(',')[0]
                print('Testing word ' + word)
                result = self.separate_syllables(word)
                output_file.write(' '.join(result) + ' - '
                                  + str(len(result)) + ' silabas\n')



if __name__ == '__main__':
    separator = Silva2011SyllableSeparator()
    if len(argv) == 1:
        separator._test()
    else:
        print(separator.separate(argv[1]))

syllable_separator = Silva2011SyllableSeparator()

