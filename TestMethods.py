#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TestMethods class provides 5 tests per class provided
"""
import unittest
from DataMuseQuerier import DataMuseQuerier
from Word import Word
from WordSubstitutor import WordSubstitutor
from SpaCyParser import SpaCyParser
from TextComplexifier import TextComplexifier

class TestMethods(unittest.TestCase):
    
    # Tests for Word class
    def test_complexity_calculator(self):
        """
        Tests that the complexity calculator works if no frequency has been input
        """
        word = Word("test","n")
        self.assertTrue(len(str(word.compute_complexity_score())) > 0)
    
    def test_get_word(self):
        """
        Check that the get_word method actually works
        """
        word = Word("test","n")
        self.assertEqual(word.get_word(), "test")

    # Test DataMuseQuerier Class
    def test_empty_query(self):
        """
        Make sure that the command still runs if an empty query is passed, but that nothing is returned
        """
        querier = DataMuseQuerier()
        self.assertEqual(querier.get_synonym_query_results(Word("","")), [])
        
    
    def test_left_context_only_query(self):
        """
        Make sure that if only left context word is given, query returns results
        """
        querier = DataMuseQuerier()
        results = querier.get_synonym_query_results(Word("the", ""), left_context = "to")
        self.assertTrue(len(results) > 0 )
    
    def test_right_context_only_query(self):
        """
        Make sure that if only right context word is given, query returns results
        """
        querier = DataMuseQuerier()
        results = querier.get_synonym_query_results(Word("the", ""), right_context = "mall")
        self.assertTrue(len(results) > 0 )
    
    def test_left_and_right_context_query(self):
        """
        Make sure that if only right context word is given, query returns results
        """
        querier = DataMuseQuerier()
        results = querier.get_synonym_query_results(Word("the", ""), left_context = "to", right_context = "mall")
        self.assertTrue(len(results) > 0 )
   
    def test_api_connection(self):
        """
        Tests to make sure that a query can be executed and return the expected results
        """
        dog = Word("dog", "n")
        querier = DataMuseQuerier()
        query_result = querier.get_synonym_query_results(dog)[0]
        expected_result = {'score': 45976, 'tags': ['syn', 'n', 'f:0.000000'], \
                           'word': 'canis familiaris'}
        self.assertEqual(query_result, expected_result)
        
    def test_query_of_upper_case(self):
        """
        Tests to make sure that a query of an upper case word returns the expected result
        """
        upper_dog = Word("DOG", "n")
        querier = DataMuseQuerier()
        query_result = querier.get_synonym_query_results(upper_dog)[0]
        expected_result = {'score': 45976, 'tags': ['syn', 'n', 'f:0.000000'], \
                           'word': 'canis familiaris'}
        self.assertEqual(query_result, expected_result)
        
    def test_query_of_mixed_case(self):
        """
        Tests to make sure that a query of a word with mixed upper and lower case 
        returns the expected result
        """
        upper_dog = Word("Dog", "n")
        querier = DataMuseQuerier()
        query_result = querier.get_synonym_query_results(upper_dog)[0]
        expected_result = {'score': 45976, 'tags': ['syn', 'n', 'f:0.000000'], \
                           'word': 'canis familiaris'}
        self.assertEqual(query_result, expected_result)
    
    
    def test_freqency_query_of_empty_word(self):
        """
        Make sure code still runs if an empty string is passed into frequency
        """
        word = Word("", "")
        querier = DataMuseQuerier()
        self.assertTrue(len(str(querier.get_frequency(word))) > 0)
        
        
    def test_frequency_query_of_fake_word(self):
        """
        Make sure a non-english word typed in still returns something and doesn't throw an error
        """
        fake_word = Word("asdfjk", "")
        querier = DataMuseQuerier()
        self.assertTrue(len(str(querier.get_frequency(fake_word))) > 0)
        
    def test_frequency_query_of_real_word(self):
        """
        Make sure our frequency querier returns the expected result for a real word
        """
        querier = DataMuseQuerier()
        self.assertEqual(querier.get_frequency(Word("dog", "n")), 63.72759)
        
    def test_best_synonym_of_empty_word(self):
        """
        Make the best_synonym function returns an empty string for an empty string
        """
        word_substitutor = WordSubstitutor()
        self.assertEqual(word_substitutor.get_best_synonym(Word("", "")).get_word()\
                         , "")
        
    def test_best_synonym_of_fake_word(self):
        """
        Make that, if a non-English word is input to the best_synonym function,
        That word is returned
        """
        word_substitutor = WordSubstitutor()
        self.assertEqual(word_substitutor.get_best_synonym(Word("asdkf", "")).get_word(),\
                         "asdkf")
    
    def test_best_synonym_without_tag(self):
        """
        Make sure get_best_synonym code still runs if no POS tag is passed
        """
        word_substitutor = WordSubstitutor()
        result_returned = len(word_substitutor.get_best_synonym(Word("dog", "")).get_word()) > 0
        self.assertTrue(result_returned)
        
    def test_best_synonym_of_real_word(self):
        """
        Make sure we get expected results for the best synonym of a common
        English word
        """
        word_substitutor = WordSubstitutor()
        result = word_substitutor.get_best_synonym(Word("dog", "n")).get_word()
        self.assertEqual(result, "hound")
        

    def test_spacy_parser_on_empty_string(self):
        """
        Make sure SpaCy Parser still runs on an emptry string
        an empty list
        """
        parser = SpaCyParser()
        result = parser.parse_and_tag_text("")
        self.assertEqual(result, [])
        
    
    def test_spacy_parser_on_punctuation(self):
        """
        Make sure SpaCyParser still runs on punctuation
        And returns puncuation (.) as the tag
        """
        parser = SpaCyParser()
        result = parser.parse_and_tag_text("?")
        self.assertEqual(result, [('?', '.')])
    
    def test_spacy_parser_on_known_sentence(self):
        """
        Make sure SpaCyParser runs as expected on
        a sentence of known tags
        """
        parser = SpaCyParser()
        result = parser.parse_and_tag_text("I like to eat lots of food")
        expected_result = [('I', 'PRP'), ('like', 'v'), ('to', 'TO'), \
                           ('eat', 'v'), ('lots', 'NNS'), ('of', 'IN'), \
                           ('food', 'n')]
        self.assertEqual(result, expected_result)
    
    def test_spacy_parser_on_mixed_text_and_punctuation(self):
        parser = SpaCyParser()
        result = parser.parse_and_tag_text("I, however, feel differently.")
        expected_result = [('I', 'PRP'), (',', ','), ('however', 'adv'), \
                           (',', ','), ('feel', 'v'), ('differently', 'adv'),\
                           ('.', '.')]
        self.assertEqual(result, expected_result)
        
    
    def test_text_complexifier_on_empty_text(self):
        """
        Make sure that the TextComplexifier class doesn't fail on empty strings,
        But returns an empty string
        """
        tc = TextComplexifier()
        self.assertEqual(tc.complexify_text(""), "")
    
    def test_text_complexifier_on_text_with_punctuation(self):
        """
        Make sure that TextComplexifier retains punctuation and
        Returns the expected output
        """
        tc = TextComplexifier()
        result = tc.complexify_text("I, however, like to think of myself as a gentleman.")
        expected_result = "I, notwithstanding, like to reckon of myself as a gent."
        self.assertEqual(result, expected_result)
    
    def test_text_complexifier_on_punctuation_only(self):
        """
        If only punctuation is passed, make sure only that punctuation is returned
        by TextComplexifier
        """
        tc = TextComplexifier()
        self.assertEqual(tc.complexify_text(","), ",")
         
    def test_text_complexifier_on_whitespace(self):
        """
        Make sure that TextComplexifier preserves whitespace if only 
        whitespace is passed
        """
        tc = TextComplexifier()
        self.assertEqual(tc.complexify_text(" "), " ")
    
    def test_text_complexifier_on_fake_word(self):
        """
        Make sure the TextComplexifier still runs with a fake word
        And returns that word
        """
        tc = TextComplexifier()
        self.assertEqual(tc.complexify_text("asdkj"), "asdkj")
        
if __name__ == '__main__':
    unittest.main()

        
        
        


