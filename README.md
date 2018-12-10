# CIT591-NLP-Nitro <img src="https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/shield-only-RGB-4k.png" width="40" hieght="40">
Making your world more complex one token at a time...

### Introduction

Our package, NLP_Nitro, provides python-based software to automatically "complexify" any provided text. Specifically, this package includes a GUI that allows the user to type in any arbitrary English text. The GUI will then return a complexified version of the text, where all non-comparator adjectives, singular non-pronoun nouns, adverbs, and verbs are replaced by synonyms of similar meaning and higher complexity.

### Background

This problem of substituting simpler words for more complex synonyms was motivated because it is a common problem with practical applications for anyone wishing to write a non-redundant and professional expsosition.

Our project would not be possible without the contributions of NAACL paper [Simple PPDB Contextual Simplification](http://cis.upenn.edu/~ccb/publications/simple-ppdb.pdf).  As an extension to prior work completed by [Reno Kris](https://rekriz11.github.io/), NLP Nitro aims to implement this research paper backwards and transform any content message into a higher complexity score ("Shakespearify" any text, if you will).  

Efforts in this research lead us down another path using an API DataMuse for better lexical substitutions for tokens in our text, but PPDB remained central to our cause and an inspiration to further growth in this project.  Whereas previous research in lexical substituion and simplification utilized nltk tokenizer and [PPDB](http://paraphrase.org/#/) for paraphrasing, our lexcial complexification model utilizes [DataMuse](https://www.datamuse.com/api/) a word finding query for engine developers and the [spaCy](https://spacy.io/) english model for tokenization and POS tagging.

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
   - `nlp = spacy.load('en')` *_ this is the full english model _*
   - `nlp = spacy.load('en_core_web_sm')`*_ this is the english mini-model _* 

### More Help
> For more help on downloading spaCy you can use [this GitHub repository](https://github.com/explosion/spaCy/issues/1721) for detailed documentation on how to deal with different issues.

### Running The Program
0. Make sure you have a Python (preferably 3) installed on your machine, have installed 'spacy' via the instructions above, and have a working internet connection.
1. Run 'main.py'.
2. Enter text for complexification as many times as you would like.
3. (Optional) Run Unit tests. You can do this before step 1 or at any point, to make sure things are functioning properly. Simply run the "TestMethods.py" file.

## Implementation Details

### Complexification Algorithm
Our complexification algorithm is based largely off of the frequency with which a given word shows up in the Google NGram Book Corpus. Specifically, a word's complexity is definined to be *e^(-frequency)*. It is a well known fact in English that a word's complexity is inversely related to it's frequency. We chose to use the negative exponential, rather than *1/(frequency)*, since the negative exponential can handle zero frequencies. Given this complexity measure, our program complexifies text as follows:

1. Given some text passed by the user, parse the text into individual tokens and add a part of speech tag. (For our purposes, tokens were just single words and seperating punctuation. Multi-word tokens were not considered for simplicity.) 
2. For each token, if the token is a non-comparator adjective, adverb, singular non-pronoun noun, or verb, query the DataMuse API and return the 5 most similar synonyms (according to the DataMuse similarity score)
3. Find the synonym that has the highest complexity score that is the same part of speech and meets a minimum similarity score to the original word. If this synonym's complexity exceeds the original word's complexity, substitute the synonym.
4. Return the resulting set of text once all tokens have been considered for substitution.

## Design
Our package involves several classes, whose relationship and summary can be found in the UML diagram below. Further details also follow.

### UML Diagram 

Feel free to scroll to view whole diagram or download PDF by maximizing window [here](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro-UML.pdf)

https://docs.google.com/viewer?url=${https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro-UML.pdf}

<img src="https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/UML.html" width="600" height="1000" />

<div>
    <iframe src="https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/UML.html&embedded=true" height="600" width="1000" allowfullscreen="" frameborder="0"></iframe>
</div>

![Model View Controller](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/UML.html)

![NLP Nitro UML](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro.png)

### main
[quick access main.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/main.py)

This is the main method in the program. When this file is run, a GUI will appear allowing the user to type in text for complexification. The complexified version of the text will be displayed, along with the original input. The user can run this as many times as he/she wishes and until he/she specifies to quit. The GUI displayed is an instance of the ComplexifierGUI class, described below.

### ComplexifierGUI Class
[quick access ComplexifierGUI.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/ComplexifierGUI.py)

ComplexifierGUI class uses the tkinter class to build a GUI allowing the user to interact with the TextComplexifier class. Specifically, provides a method that allows the user to type in text in a pop up window, and returns the complexified text in another pop up. Also provides a button allowing the user to continue for as many iterations as they would like.

### TextComplexifier Class
[quick access TextComplexifier.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/TextComplexifier.py)

This is the main class prior to interacting with the GUI. TextComplexifier provides a method to take in a String (sequence of text) and return a new piece of complexified text. It feeds input into and stitches output from the SpaCyParser and WordSubstitutor classes.

### SpaCyParser Class
[quick access SpaCyParser.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/SpaCyParser.py)

SpaCyParser is where all the *magic* starts to happen.  It takes in a content messaged passed from the TextComplexifier class and starts getting to work!  By default, spaCy will parse each token in a text and label it with a variety of categories including, but not limited to TEXT, LEMMA, POS, TAG, DEP, SHAPE, ALPHA, STOP, Dependency Parse, tokenization, Sentence Segmentation, and rules-based matching (to name a few).  In this class we solely deal with TEXT, POS, and TAG.  Once the universal tags are parsed into the text, we then do a conversion from spaCy's POS tag convention to DataMuses's POS tag convention so that we can properly query the API.

A text is then parsed into two list of tuples (token and corresponding POS tag), and then enumerated to put all tokens of interest into it's own consolidated list that can be later traversed and searched with an integer key that corresponds to it's token placement with in the sentence.  This makes it uniquely suitable for lexical substitution once the complexity score is calculated.  It has 3 instance variables: __nlp (English model from spaCy), tokens (list), and tags (list).

SpacyParser has one magical method called parse_and_tag_text() that receives a text, tokenizes, and returns api_tags, a list of tuples of (word, DataMuse_formatted_POS).

### WordSubstitutor Class
[quick access WordSubstitutor.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/WordSubstitutor.py)

WordSubstitutor class works hand-in-hand with SpaCyParser class to give TextComplexifier class the best possible synonym selections of a higher complexity score to work with.  WordSubstitutor takes in a Word object and provides a method to return a word of similar meaning and higher complexity substituted. Only substitutes for verbs, non-comparitor adjectives, adverbs, and non-pronoun nouns are considered.

WordSubstitutor has one method get_best_synonym() that takes in a Word object, looks at the top 5 synonyms according to DataMuse API, and finally returns the word with the most complex synonym. If the most complex word is the original, that word is returned.  If not, the higher-complexity-scored word is returned.

### DataMuseQuierier Class
[quick access DataMuseQuierier.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/DataMuseQuerier.py)

If you haven't felt the *magic* yet after SpaCyParser and WordSubstitutor, then you'll definitely feel the magic now with DataMuseQuierier. DataMuseQuerier queries the datamuse API for the synonyms of a given word and returns the top 5 results. Also provides a method to query the API and return the frequency of a given word.

*Some additional background*
As previously mentioned, prior research has used nltk parser and PPDB to generate acceptable paraphrases for unigram, bigram, trigram lexical substitution and is widely used in NLP literature.  For this project, we decided to apply the principles of PPDB to an API as a our standard pool of wonderful tokens to cherry pick from in WordSubstitutor. 

### Word Class
[quick access Word.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/Word.py)

Word class holds the properties of an English word. Specifically, for each word, the class stores the actual token (String), the corresponding POS, and frequency of use in the Google Ngram Books Corpus. Aside from its getters and setters, the only method for Word class is compute_complexity_score(), which returns a word's complexity score (or *e^(-frequency)*).

### TestMethods Class
[quick access TestMethods.py](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/TestMethods.py)

This class provides unit tests for all classes in the NLP_Nitro package, with the exception of ComplexifierGUI and main. 25 total unit tests are provided, roughly 5 per class. Tests largely ensure that blank strings, non-words, and punctuation don't cause errors. They also check that various functions return output as expected. 

*To run these unit tests, simply run the file*
 







