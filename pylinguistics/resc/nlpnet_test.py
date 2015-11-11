import nlpnet
tagger = nlpnet.POSTagger('/path/to/pos-model/', language='pt')
tagger.tag('O rato roeu a roupa do rei de Roma.')
#[[(u'O', u'ART'), (u'rato', u'N'), (u'roeu', u'V'), (u'a', u'ART'), (u'roupa', u'N'), (u'do', u'PREP+ART'), (u'rei', u'N'), (u'de', u'PREP'), (u'Roma', u'NPROP'), (u'.', 'PU')]]