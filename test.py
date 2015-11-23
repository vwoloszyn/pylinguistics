#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append("./pylinguistics/")

import Pylinguistics as pl







text = "Houve um tempo em que o hábito de manter cadernos de anotações era algo bastante corriqueiro. Os chamados de 'livros de lugares-comuns' (ou commonplace books ) eram utilizados pelos leitores para o registro de trechos e passagens interessantes com que se deparavam em suas leituras. Mas além de transcrições, esses cadernos também reuniam apontamentos sobre a vida cotidiana, conforme relata o historiador Robert Darnton em A Questão dos Livros (Cia. das Letras, 2009, p.164). Essas informações eram grupadas e reorganizadas à medida que novos excertos iam sendo acrescidos. O hábito espalhou-se por toda a Inglaterra no início da era Moderna, e muitos escritores famosos - entre eles John Milton e Francis Bacon - cultivaram essa maneira especial de absorver a palavra impressa, fundada na não linearidade e na fragmentação da informação. "
text = "Os benefícios concedidos pela FAPESP para bolsas de doutorado e pós-doutorado no Exterior foram alterados a partir do mês passado. Assim, o valor básico da manutenção passou de US1.400paraUS1700 mensais; o benefício para instalação, em casos de bolsas com duração de seis meses ou mais, foi elevado de US1.000paraUS 1.200 e a ajuda de custo para cobertura de despesas com saúde passou de US100paraUS 150 mensais. \n Foram alterados também os adicionais concedidos a bolsistas com dependentes. Dessa forma, quem tem um dependente recebe agora adicional de US250,contraosUS 200 em vigor até o final de junho; para dois dependentes, o adicional passou de US350paraUS 450; em caso de três dependentes, ele foi elevado de US450paraR 600 e para quatro dependentes ou mais, passou de US500paraUS 700 mensais. \n As bolsas no País permanecem com os mesmos valores vigentes desde fevereiro passado: iniciação científica, R250;aperfeiçoamento,R 500; mestrado I (fase inicial), R700;mestradoIIR750; doutoramento I, R1.050;doutoramentoII,R1.300 e pós-doutoramento R$ 1.900."
#text= "Ia bem em matemática, porém reprovou em física."
#text =  "Vou começar a chorar"
#text = "O rato roeu a roupa do rei de Roma."
objpl=pl.text(text)
objpl.setLanguage("pt-br");

print('Features: %s' %objpl.getFeatures())
print('POS_TAGS: %s' %objpl.postag)


