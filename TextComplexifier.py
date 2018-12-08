#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TextComplexifier is the main class.
Provides a method to take in a String (sequence of text)
and returns a new piece of text with the same meaning and 
nouns, verbs, adjectives, and adverbs substituted for more complicated
synonyms
"""

from Word import Word
from WordSubstitutor import WordSubstitutor
from SpaCyParser import SpaCyParser
import re

class TextComplexifier:
    
    def __init__(self):
        """
        Constructor initializes a querier, parser, and WordSubstitutor
        """
        self.__parser = SpaCyParser()
        self.__word_substitutor = WordSubstitutor()
        
    def __vec_to_string(self, text_vector):
        """
        (Private) helper method to convert a vector of strings and punctuation
        to one single string
        """
        
        # if the text vector is blank, return a blank string
        if len(text_vector) == 0:
            return ''
    
        # Make sure code doesn't break with index out of bounds error for single
        #   word vectors
        elif len(text_vector) == 1:
            return text_vector[0]
        
        else:
            output_text = text_vector[0]
            non_character = re.compile('\W')
            for token in text_vector[1:]:
                # Don't add a space before character if punctuation
                if re.match(non_character, token):
                    output_text = output_text + token
                
                # If the token is a number or word, add a space before
                else:
                    output_text = output_text + ' ' + token
    
            return output_text
        
    def complexify_text(self, text):
        """ Main method that takes in text and returns text of the same meaning
            and higher complexity
        
        Args:
            text: String (of text) to be analyzed
        
        
        Returns:
            a more complex String of text with the same meaning
        """
        
        output_vec = []
        parsed_words_and_tags = self.__parser.parse_and_tag_text(text) # parse text
        
        # substitute words for complex words
        for token in parsed_words_and_tags:
            word = Word(token[0], token[1])
            output_vec.append(self.__word_substitutor.get_best_synonym(word).get_word())
        
        # convert vector to string and return
        return self.__vec_to_string(output_vec)