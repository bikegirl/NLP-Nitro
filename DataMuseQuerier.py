#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests

"""
DataMuseQuerier Class queries the datamuse API for the synonyms of a given word
Returns top 5 results. Also provides a method to query and return frequency 
for a given word.
"""

class DataMuseQuerier:
    
    def __init__(self):
        self.__api_url = "https://api.datamuse.com/words?"
    
    def get_synonym_query_results(self, word, left_context = "", right_context = ""):
        """Takes in an object of the class Word and returns the top 5 synonyms
           Optionally can specify left and right context (as strings)
          
        Args:
            word: Word object whose synonyms the user wants to find
            left_context: optionally specified string as left context
            right_context: optionally specified string as right context
        
        Returns:
            API query results as a list
        """
        if (len(left_context) == 0) and (len(right_context) == 0):
            response = requests.get(self.__api_url + 'ml=' + word.get_word() + '&md=f&max=5')
            return json.loads(response.content.decode('utf-8'))
        
        # Add left context if it's available
        elif (len(left_context) > 0) and (len(right_context) == 0):
            response = requests.get(self.__api_url + 'ml=' + word.get_word() + \
                                    '&lc=' + left_context + '&md=f&max=5')
            return json.loads(response.content.decode('utf-8'))
        
        # Add right context if it's available
        elif (len(left_context) == 0) and (len(right_context) > 0):
            response = requests.get(self.__api_url + 'ml=' + word.get_word() + \
                                    '&rc=' + right_context + '&md=f&max=5')
            return json.loads(response.content.decode('utf-8'))
        
        # Add both left and right contexts, if avialable
        else:
            response = requests.get(self.__api_url + 'ml=' + word.get_word() + \
                                    '&lc=' + left_context + '&rc=' + right_context\
                                    + '&md=f&max=5')
            return json.loads(response.content.decode('utf-8'))
            
    
    def get_frequency(self, word):
        """ Queries the API and returns the frequency of one individual word
        
        Args:
            word: Word object whose freqeuncy we want to find
        
        Returns:
            frequency: float - the word's frequency in Google NGrams
        
        """
        response = requests.get(self.__api_url + 'sp=' + word.get_word() + '&md=f&max=1')
        parsed_json = json.loads(response.content.decode('utf-8'))
        
        # Make sure that there is something returned
        if len(parsed_json) > 0:
            return float(parsed_json[0]['tags'][0].split(":")[1])
        
        # if the word is a nonempty string and nothing is returned, consider it rare because it wasn't found
        elif len(word.get_word()) > 0:
            return 0 
        
        # return "infinite frequency" to never use this word an empty String is passed
        else:
            return float('inf') 
    
    
        
        
        
        
        

