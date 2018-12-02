#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word class holds the properties of a word:
    part_of_speech, and has a method for computing
"""
import math

class Word:
    
    def __init__(self, word, part_of_speech, frequency = 0):
        self.__word = word
        self.__part_of_speech = part_of_speech
        self.__frequency = frequency
    
    def set_frequency(self, frequency):
        self.__frequency = frequency
    
    # Get word
    def get_word(self):
        return self.__word
    
    def get_part_of_speech(self):
        return self.__part_of_speech
    
    def get_frequency(self):
        return self.__frequency

    def compute_complexity_score(self):
        """
        For now, word complexity is just 1/frequency
        % MAYBE ADD MODEL AND OR LENGTH LATER
        """
        # return len(self.__word)
        
        return math.exp(-self.__frequency)


