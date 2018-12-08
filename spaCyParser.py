#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpaCy Parser; Add comments later

To install: pip install -U spacy && python -m spacy download en
"""
import spacy

class SpaCyParser:
    
    def __init__(self):
        """
        Constructor:
            Load English tokenizer, tagger, parser, NER and word vectors
            import model 'en_core_web_sm' and assign to object
        """
        self.__nlp = spacy.load('en_core_web_sm')
        self.__tokens = []
        self.__tags = []
    
    
    def parse_and_tag_text(self, text):
        """
        Args:
            text: a String (sequence of text)
            
        Returns:
            A list of touples, containing (token, POS). A token is any word or
            punctuation character
        """
        doc = self.__nlp(text); # spaCy tokenize sentence

        ## POS-tag
        for token in doc:
            self.__tokens.append(token.text)
            self.__tags.append((token.text, token.tag_))


        ## convert tags to API equivalent for DataMuse
        api_tags = []
        for item in self.__tags:
            if item[1] in ('JJ', 'JJS'):
                api_tags.append((item[0], 'adj'))
            elif item[1] in ('NN', 'NNS'):
                api_tags.append((item[0], 'n'))
            elif item[1] in ('RB', 'RBR', 'RBS', 'ADV'):
                api_tags.append((item[0], 'adv'))
            elif item[1] in ('VBG', 'VB', 'VBN', 'VBP', 'VBZ'):
                api_tags.append((item[0], 'v'))
            else:
                api_tags.append(item)

        # Now clear __tags and __tokens for future use
        self.__tags = []
        self.__tokens= []
       
        # Return API tags
        return api_tags
