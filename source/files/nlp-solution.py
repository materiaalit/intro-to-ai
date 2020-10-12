# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import spacy
from spacy.symbols import nsubj, VERB
nlp = spacy.load('en')

# open the file and parse it using the English grammar ('en')
source = open("metamorphosis.txt").read()
doc = nlp(source)

verbs = {}
# iterate over the sentences in the document
for sent in doc.sents:
    # check that the root of the sentence is a verb
    if sent.root.pos == VERB:
        # make note of the basic form of the verb
        verb = sent.root.lemma_

        # iterate over words in the sentence
        
        for word in sent:
            if word.text == 'Gregor' and word.dep == nsubj and word.head == sent.root:
                print("%20s :: %s" % (verb, sent.text[:60]))
                if not verb in verbs:
                    verbs[verb] = 0
                verbs[verb] = verbs[verb]+1

# print out the verbs that have count > 0 in the order of decreasing 
# frequency, so that the most popular verb is printed first, etc.
# the list should begin as follows:
# say: 10
# have: 7
# be: 5

for (c,verb) in sorted(((c,verb) for verb,c in verbs.items()), reverse=True):
    print("%s: %d" % (verb,c))
