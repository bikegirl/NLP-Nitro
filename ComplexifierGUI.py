#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ComplexifierGUI class uses the tkinter class to build a GUI allowing the user
to interact with the TextComplexifier class. Specifically, provides a method
that allows the user to type in text in a pop up window, and returns the complexified
text in another pop up. Also provides a button allowing the user to continue for as many
iterations as they would like.
"""
import tkinter as tk
from tkinter import simpledialog
from TextComplexifier import TextComplexifier

class ComplexifierGUI:
    
    def __init__(self):
        self.__application_window = tk.Tk(screenName = 'Text Complexifier')
        self.__text_complexifier = TextComplexifier()
        
    def __complexify_and_display_text(self):
        """(Private) method that asks user for text in a pop up,
        computes the complexified version of that text, then 
        prints both the original text and the complexified text in a new pop up
        """
         # Ask user for input
        input_text = simpledialog.askstring("Text Complexifier", \
                                            "Please enter some text you would like complexified.",
                                            parent=self.__application_window)
        
        #Complexify Text
        complexified_text = self.__text_complexifier.complexify_text(input_text)
        
        # Display Results
        message_text = "Input text: " + input_text +  \
                        '\n\n' + "Complexified text: " + complexified_text
        
        message = tk.Message(self.__application_window, text = message_text, bg = 'lightblue', \
                             font=('times', 20, 'italic'))
        message.pack()
        
    def run_complexifier_GUI(self):
        """
        Main method of the GUI
        Allows the user to specify as many times as they would like to get text complexification
        For each time, the private method above is run
        """
        next_round = True
        while next_round == True:
            self.__complexify_and_display_text()
            next_round = tk.messagebox.askyesno("Text Complexifier", "Would you like to enter a new message?")
        tk.mainloop()
    






   

