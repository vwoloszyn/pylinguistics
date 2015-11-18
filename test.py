#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append("./pylinguistics/")

import Pylinguistics as pl







text = "Houve um tempo em que o hábito de manter cadernos de anotações era algo bastante corriqueiro. Os chamados de 'livros de lugares-comuns' (ou commonplace books ) eram utilizados pelos leitores para o registro de trechos e passagens interessantes com que se deparavam em suas leituras. Mas além de transcrições, esses cadernos também reuniam apontamentos sobre a vida cotidiana, conforme relata o historiador Robert Darnton em A Questão dos Livros (Cia. das Letras, 2009, p.164). Essas informações eram grupadas e reorganizadas à medida que novos excertos iam sendo acrescidos. O hábito espalhou-se por toda a Inglaterra no início da era Moderna, e muitos escritores famosos - entre eles John Milton e Francis Bacon - cultivaram essa maneira especial de absorver a palavra impressa, fundada na não linearidade e na fragmentação da informação. "

text= "Ia bem em matemática, porém reprovou em física."

objpl=pl.text(text.decode('utf-8'))
objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
print('POS_TAGS: %s' %objpl.postag)


