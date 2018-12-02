#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tester code to generate a set of replacements in a sentence
"""
from DataMuseQuerier import DataMuseQuerier
from Word import Word
from WordSubstitutor import WordSubstitutor

querier = DataMuseQuerier()
test_sentence = "Wow you threw that ball very far"
#test_sentence = "I ate a delicious and big ham sandwich with cheese for lunch"
# WORRY ABOUT PUNCTUATION AND PARSING LATER
sentence_vector = test_sentence.split(' ')
# get left and right contexts
left_contexts = [""]*len(sentence_vector)
for i in range(1,len(sentence_vector)):
    left_contexts[i] = sentence_vector[i-1]
    
right_contexts = [""]*len(sentence_vector)
for i in range(0, len(sentence_vector)-1):
    right_contexts[i] = sentence_vector[i+1]

parts_of_speech = ['adj', 'pron', 'v', 'art', 'n', 'adv', 'adv']
#parts_of_speech = ['pron', 'v', 'art', 'adj', 'conj', 'adj', 'n', 'n', 'prep', 'n', 'art', 'n']
output_vec = []
wsub = WordSubstitutor()
for i in range(len(sentence_vector)):
    word = Word(sentence_vector[i], parts_of_speech[i])
    word.set_frequency(querier.get_frequency(word))
    #output_vec.append(wsub.get_best_synonym(word, left_contexts[i], right_contexts[i]).get_word())
    output_vec.append(wsub.get_best_synonym(word).get_word())

    
print(output_vec)



