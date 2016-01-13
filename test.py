#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
sys.path.append("./pylinguistics/")

import Pylinguistics as pl
import pandas as pd



#fapesp=pd.read_csv('fa.csv')

#print(fapesp.loc[267]['texto'])


#text = "An auxiliary verb is most generally understood as a verb that helps another verb by adding grammatical information to it."
#text = "Os benefícios concedidos pela FAPESP para bolsas de doutorado e pós-doutorado no Exterior foram alterados a partir do mês passado. Assim, o valor básico da manutenção passou de US1.400paraUS1700 mensais; o benefício para instalação, em casos de bolsas com duração de seis meses ou mais, foi elevado de US1.000paraUS 1.200 e a ajuda de custo para cobertura de despesas com saúde passou de US100paraUS 150 mensais. \n Foram alterados também os adicionais concedidos a bolsistas com dependentes. Dessa forma, quem tem um dependente recebe agora adicional de US250,contraosUS 200 em vigor até o final de junho; para dois dependentes, o adicional passou de US350paraUS 450; em caso de três dependentes, ele foi elevado de US450paraR 600 e para quatro dependentes ou mais, passou de US500paraUS 700 mensais. \n As bolsas no País permanecem com os mesmos valores vigentes desde fevereiro passado: iniciação científica, R250;aperfeiçoamento,R 500; mestrado I (fase inicial), R700;mestradoIIR750; doutoramento I, R1.050;doutoramentoII,R1.300 e pós-doutoramento R$ 1.900."
#text= "Ia bem em matemática, porém reprovou em física."
#text =  "Todos esses que aí estão atravancando meu caminho, eles passarão... Eu passarinho!"
#text = "O rato roeu a roupa do rei de Roma."
#text = "Esse processo mostra que estamos diante de um novo modelo de interação universidade-empresa para geração de tecnologia e contratações de nível qualificado. Sabemos que no mundo a maior parte das pesquisas é feita nas empresas, mas não dá para a empresa surgir do nada. Mesmo em países como os Estados Unidos é preciso começar na universidade com ideias inovadoras, diz Pereira. Para os contratados, a parceria se transformou em uma grande oportunidade de exercício profissional. Sempre quis trabalhar no ramo empresarial e em desenvolvimento sustentável, diz a bióloga Maria Grassi, 25 anos."
#objpl=pl.text(fapesp.loc[267]['texto'].decode('utf-8'))

file = open('english/2286.txt', 'r')


text = file.read()

print text

objpl = pl.text(text)


objpl.setLanguage("en");


print('Features: %s' %objpl.getFeatures())
#print('POS_TAGS: %s' %objpl.tokens)
print('POS_TAGS: %s' %objpl.postag)
#print(len(objpl.postag))


 