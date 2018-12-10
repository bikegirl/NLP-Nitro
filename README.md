# CIT591-NLP-Nitro
Making your world more complex one token at a time...

### Introduction

Our project would not be possible without the contributions of NAACL paper [Simple PPDB Contextual Simplification](http://cis.upenn.edu/~ccb/publications/simple-ppdb.pdf).  As an extension to prior work completed by [Reno Kris](https://rekriz11.github.io/), NLP Nitro aims to implement this research paper backwards and transform any content message into a higher complexity score ("Shakespearify" any text, if you will).  

Efforts in this research lead us down another path using an API DataMuse for better lexical substitutions for tokens in our text, but PPDB remained central to our cause and an inspiration to further growth in this project.  Whereas previous research in lexical substituion and simplification utilized nltk tokenizer and [PPDB](http://paraphrase.org/#/) for paraphrasing, our lexcial complexification model utilizes [DataMuse](https://www.datamuse.com/api/) a word finding query for engine developers, GUIbuilder library, and the [spaCy](https://spacy.io/) english model for tokenization and POS tagging.

### Depedencies

- In your python environment, you must install spaCy by going to [spaCy website: linguistic features documentation](https://spacy.io/usage/linguistic-features).  
- Although this should work with anything higher than **python 2.6**, we recommend **python 3** for running this project (I used Python 3.6 and my partner uses Python 3.5).  

### Downloading spaCy
> `import spaCy`

> Change directory be in working project folder

> use `pip install -U spacy && python -m spacy download en`

### Common Errors
1. the encoding for reading in a file.  Be sure to encode with UTF-8.  If you get an error that says something to the effect of "not recognizing ASCII characters," this is why. 
2. Project interpreters in your IDE (i.e. - PyCharm, Spyder).  Ensure you cd to the working directory of your project in command line.  Once you've set the right directory in command line run "python" to ensure you are using python 2.6 or higher.  If it turns out you are not running the correct Python, you must download at this time.
3. Path not found, file not found.  This means although you many have downloaded spaCy, you did not download it to the interpreter you thought you did.  You select correct python for your interpreter and then see (2) as reference.  Switch to working directly, verify which Python is being linked to the working directory, if not correct Python download accordingly. 
4. Cannot fine module en or couldn't link model.  You must use a seperate command to download the English model, try these two versions because it depends on an individual basis how you set up your environment and where you set the pathway to your python download (whether default or you selected custom location):
   - `nlp = spacy.load('en')`//this is the full english model
   - `nlp = spacy.load('en_core_web_sm')`//this is the english mini-model 

### More Help
> For more help on downloading spaCy you can use [this GitHub repository](https://github.com/explosion/spaCy/issues/1721) for detailed documentation on how to deal with different issues.

## NLP Nitro Project

### UML Diagram - a brief overview

Feel free to scroll to view whole diagram or download PDF by maximizing window [here](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro-UML.pdf)

![NLP Nitro UML](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro.png)

### Main

This is not the main method.  File is called Main.py. ComplexifierGUI helper function the has a ComplexiferGUI object to call run GUI method.

### ComplexifierGUI Class

Serves as a graphical user interface between the User in order to hide implementation details of the program.  The class has 2 instance variables: called __application_window that displays the title for the TextWidget and __text_complexifier which is a TextComplifier object.  For all intents and purposes you can think of ComplexifierGUI Class as codependent with main, (helper function of main), as main is called through the GUI or via GUI.

Methods include __complexify_and_display_text and run_complexifier_GUI.  
-__complexify_and_display_text will display the output vector un by run_complexifier_GUI 
- run_complexifier GUI will return the output vector after processing to be displayed to the GUI.

### TextComplexifier Class

This is the main method by all conventional standards.  At a high-fully encapsulated level TextComplexifier provides a method to take in a String (sequence of text) and returning a new piece of text, it depends directly upon the SpacyParser and WordSubstitutor Class for all the brains behind the work.  Carefully selected parts of speech (nouns, verbs, adjectives, and adverbs) are substituted for more complicated synonyms based off a complexity score while preserving the meaning of the overall message.

TextComplexifier Class takes in a SpaCyParser Object and a WordSubstitutor Object in order to access methods needed to complexify text.  TextComplexifier has two methods: __vec_to_string and complexify_text.
- __vec_to_string helper method to convert a vector of strings and punctuation to one single string
- complexify_text a method that takes in a text and returns a string with a higher complexity score while preserving the meaning.

### SpaCyParser

SpaCyParser is where all the *magic* starts to happen.  It takes in a content messaged passed from the TextComplexifier class and starts getting to work!  By default, spaCy will parse each token in a text and label it with a variety of categories including, but not limited to TEXT, LEMMA, POS, TAG, DEP, SHAPE, ALPHA, STOP, Dependency Parse, tokenization, Sentence Segmentation, and rules-based matching (to name a few).  In this class we solely deal with TEXT, POS, and TAG.  Once the universal tags are parsed into the text, we then do a comparison with DataMuses's POS tag convention so that we can select higher scoring synonyms and match them up with the POS tag that DataMuse Provides.

A text is then parsed into two list of touples (token and corresponding POS tag), and then enumerated to put all tokens of interest into it's own consolidated list that can be later traversed and searched with an integer key that corresponds to it's token placement with in the sentence.  This makes it uniquely suitable for lexical substitution once the complexity score is calculated.  It has 3 instance variables, __nlp english model from spaCy, tokens[] list, and tags[] list.

SpacyParser has one magical method called parse_and_tag_text() that receives a text, tokenizes, and returns api_tags (a list of tuples) of the correct POS equivalents to DataMuse.

### WordSubstitutor

WordSubstitutor Class works hand in hand with SpaCyParser class to give TextComplexifier class the best possible synonym selections of a higher complexity score to work with.  WordSubstitutor takes in a Word, provides a method to return the sentence with words of appropriate higher complexity.  It receives a DataMuseQuierer Object as an instance variable and only substitutes for verbs, non-comparator adjecticves, adverbs, and non-pronoun nouns.

WordSubstitutor has one method get_best_synonym Takes in a Word object, looks at the top 5 synonyms according to DataMuse API, 0then returns the word with the most complex synonym. If the most complex word is the original, that word is returned.  If not, the higher complexity scored word is returned.





