#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WordSubstitutor class takes in a word
splits the words based on whitespace and all punctuation except "'". 
Provides a method to return the sentence with words of appropriate higher complexity
Substituted
"""
from Word import Word
from DataMuseQuerier import DataMuseQuerier

# Maybe change to a Sentence class input later or a string of words
class WordSubstitutor:
    
    # constructor
    def __init__(self):
        self.__synonym_querier = DataMuseQuerier()
    
    # substitute words
    # ADD IN AN ARGUMENT FOR CHECKING STOP WORDS LATER
    def get_best_synonym(self, word, left_context = "", right_context = ""):
        """ Takes in a Word obejct, looks at the top 5 synonyms according to DataMuse API,
            then returns the word witht the most complex synonym. 
            If the most complex word is the original,
            that word returnsed
        """
        # Only looks for synonyms if word is not an article, conjunction, or pronoun
        # Maybe change to add stop list later
        if word.get_part_of_speech() in ['art', 'conj', 'pron', 'prep']:
            return word
        
        else:
            # Query results from API = synonym list, with part of speech tags
            synonym_list = self.__synonym_querier.get_synonym_query_results(word, left_context, right_context)
            
            best_synonym = Word("", "")
            max_synonym_score = 0
            for syn in synonym_list:
                
                # If synonym is same part of spech, compute complexity
                if word.get_part_of_speech() in syn['tags']:
                    
                    # only consider word if "score" > 20000
                    score = syn['score']
                    if score < 20000:
                        pass
                    else:
                        freq = float(syn['tags'][len(syn['tags']) - 1].split(':')[1])
                        synonym = Word(syn['word'], word.get_part_of_speech(), freq)
                        syn_score = synonym.compute_complexity_score()
                        
                        if syn_score > max_synonym_score:
                            best_synonym = synonym
                            max_synonym_score = syn_score
        
        
            # Now check if best synonym is more complex than original word
            if max_synonym_score > word.compute_complexity_score():
                word = best_synonym
            
            return word
            
# Example code:
# test_word = Word("dog", "n")
# word_sub = WordSubstitutor()
# test_word = word_sub.get_best_synonym(test_word)
# print(test_word.get_word()) --> prints 'canis familiaris'
            