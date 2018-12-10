#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tester code to generate a set of replacements in a sentence
"""
from DataMuseQuerier import DataMuseQuerier
from Word import Word
from WordSubstitutor import WordSubstitutor
from SpaCyParser import SpaCyParser
import re

querier = DataMuseQuerier()
parser = SpaCyParser()
wsub = WordSubstitutor()

#test_sentences = "Wow you threw that ball very far. \
#                  I ate a delicious and big ham sandwich with cheese for lunch \
#                  The pretty girl was very worried about the difficult final exams coming up.\
#                  She would like more than anything to take a nap."

output_vec = []
parsed_words_and_tags = parser.parse_and_tag_text(test_sentences)
for token in parsed_words_and_tags:
    word = Word(token[0], token[1])
    #output_vec.append(wsub.get_best_synonym(word, left_contexts[i], right_contexts[i]).get_word())
    output_vec.append(wsub.get_best_synonym(word).get_word())

print(output_vec)

# Now concatinate:
output_text = output_vec[0]
non_character = re.compile('\W')
for token in output_vec[1:]:
    # Don't add a space before character if punctuation
    if re.match(non_character, token):
        output_text = output_text + token
    
    # If the token is a number or word, add a space before
    else:
        output_text = output_text + ' ' + token
    

print(output_text)