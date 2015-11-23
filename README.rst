Pylinguistics
~~~~~~~~~~~~~

``Pylinguistics`` is a biligual (Portuguese and English) linguistics tool inspired on http://cohmetrix.com/ that allows an analysis of cohesion, coherence of a text. In reading and comprehension process, the textual cohesion is an important characteristics that help the reader to mentally connect tue ideas expressed in the text (Graesser, McNamara, & Louwerse, 2003). ``Pylinguistics`` is a open source project that allows educators, researchers and developers compute readability of texts.

Metrics
~~~~~~~~~~~~~

The project is still in developing process, but until now, we already have some functional metrics.

* Word count
* Sentence count
* Word_per_sentence
* Syllable count
* Average of syllables per word
* Adjective Incidence
* Noun Incidence
* Verb Incidence
* Adverbs Incidence
* Pronoun Incidence
* Content words Incidence
* Functional word Incidence
* Lexical Diversty
* Content word Diversty
* Logic Negation Incidence
* Logic If Incidence
* Logic Or Incidence
* Logic And Incidence
* Logic Operators Incidence
* Connective Incidence
* Connective Additive Incidence
* Connective Logic Incidence
* Connective Temporal Incidence
* Connective Casual Incidence


Basicic Usage
~~~~~~~~~~~~~

.. code-block:: python

    >>> import Pylinguistics as pl
    >>> objpl=pl.text('Ia bem em matemática, porém reprovou em física.')
    >>> objpl.setLanguage("pt-br")
    >>> objpl.getFeatures()
    {'ConnectiveAdditiveIncidence': 125.0, 'redability': 66.6, 'word_count': 8, 'ConnectiveLogicIncidence': 0.0, 'syllable_count': 17, 'avg_word_per_sentence': 8.0, 'LogicIfIncidence': 0.0, 'LogicAndIncidence': 0.0, 'ContentDiversty': 1.0, 'pronIncidence': 0.0, 'LogicOperatorsIncidence': 0.0, 'verbIncidence': 250.0, 'functionalIncidence': 375.0, 'nounIncidence': 250.0, 'LogicOrIncidence': 0.0, 'adjectiveIncidence': 0.0, 'LogicNegationIncidence': 0.0, 'contentIncidence': 625.0, 'ConnectiveIncidence': 125.0, 'avg_syllables_per_word': 2.125, 'ConnectiveTemporalIncidence': 0.0, 'sentence_count': 1, 'ConnectiveCasualIncidence': 0.0, 'advIncidence': 125.0, 'LexicalDiversty': 0.9}


Dependencies
~~~~~~~~~~~~~

``Pylinguistics`` requires NLTK_ and nlpnet_. Additionally, it needs to download some data from NLTK. After installing it, call

.. _NLTK: http://www.nltk.org
.. _nlpnet: https://github.com/erickrf/nlpnet/

Try
~~~~~~~~~~~~~

You can test ``pylinguistics``by yourself without instalation: http://app.mybinder.org/1746087056/notebooks/pylinguistics_test.ipynb


Install (not working yet)
~~~~~~~~~~~~~

pip install git+git://github.com/vwoloszyn/pylinguistics.git
