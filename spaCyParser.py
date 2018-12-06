import os
import spacy
from typing import List, Any

sentence = u'The pretty girl was very worried about the difficult final exams coming up.  She would like more than anything to take a nap.'

# Load English tokenizer, tagger, parser, NER and word vectors
# import model 'en_core_web_sm' and assign to object
nlp = spacy.load('en_core_web_sm')
tokens = []
tags = []

# spaCy tokenize sentence
doc = nlp(sentence)
print(doc.ents)  # is Empty
## POS-tag
for token in doc:
    tokens.append(token.text)
    tags.append((token.text, token.tag_))

## find adjectives, nouns, verbs, and adverbs
all_pos = {}
for token, tag in enumerate(tags):
    word, postag = tag
    if (postag == 'JJ' or postag == 'VBG' or postag == 'NN' or postag == 'ADV'):
        all_pos[token] = word.lower()

## convert tags to API equivalent for DataMuse
api_tags = []
for item in tags:
    if item[1] == 'JJ':
        api_tags.append((item[0], 'adj'))
    elif item[1] == 'NN':
        api_tags.append((item[0], 'n'))
    elif item[1] == 'ADV':
        api_tags.append((item[0], 'adv'))
    elif item[1] == 'VBG':
        api_tags.append((item[0], 'v'))
    else:
        api_tags.append(item)

## convert all_pos to API equivalent for DataMuse
api_all_pos = {}
for token, tag in enumerate(api_tags):
    word, postag = tag
    if (postag == 'adj' or postag == 'n' or postag == 'adv' or postag == 'v'):
        api_all_pos[token] = word.lower()

print('\n')
print(tags)  # tokenized words with POS
print('\n')
print(all_pos)  # just the enumerated tokens
print('\n')
print(api_tags)  # same as tags but with the DataMuse tag equivalent
print('\n')
print(api_all_pos)  # same as tags but with the DataMuse tag equivalent

"""
for token, tag in tags

    orig_word = adjectives[i]
    score = socal.get(orig_word, None)
    print("(Original Word, Score: ", orig_word,"/", score,")")
    if score is None:
        print ("Could not find original adjective for *",orig_word, "* in SO-CAL", '\n')
        continue
    # go through the syn_set; for each synonym in syn_set, if socal score for the synonym is higher than the original score, add it to bettersyns
    for item in syn_set:
        newScore = socal.get(item, -10)
        if score < newScore:
            #print out all words and their scores for items that meet criteria
            print (item, newScore)
            if i not in bettersyns:
                bettersyns[i] = set()
            bettersyns[i].add(item)

#print ('\n',adjectives)"""
