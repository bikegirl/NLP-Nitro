#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ComplexifierGUI class uses the tkinter GUI-builder interface to 
"""
import tkinter as tk
from tkinter import simpledialog
from TextComplexifier import TextComplexifier

class ComplexifierGUI:
    
    def __init__(self):
        self.__application_window = tk.Tk(screenName = 'Text Complexifier')
        self.__text_complexifier = TextComplexifier()
        
    def __complexify_and_display_text(self):
         # Ask user for input
        input_text = simpledialog.askstring("Text Complexifier", \
                                            "Please enter some text you would like complexified.",
                                            parent=self.__application_window)
        
        #Complexify Text
        complexified_text = self.__text_complexifier.complexify_text(input_text)
        
        # Display Results
        message_text = "Input text: " + input_text +  \
                        '\n\n' + "Copmlexified text: " + complexified_text
        
        message = tk.Message(self.__application_window, text = message_text, bg = 'lightblue', \
                             font=('times', 20, 'italic'))
        message.pack()
        
    def run_complexifier_GUI(self):
        next_round = True
        while next_round == True:
            self.__complexify_and_display_text()
            next_round = tk.messagebox.askyesno("Text Complexifier", "Would you like to enter a new message?")
        tk.mainloop()
    






   

