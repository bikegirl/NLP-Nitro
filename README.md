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
4. Cannot fine module en or couldn't link model.  You must use a seperate command to download the English model, try these two version b/c it depends on an individual basis how you set up your environment and where the pathway to your python download is located:
   - `nlp = spacy.load('en')`//this is the full english model
   - `nlp = spacy.load('en_core_web_sm')`//this is the english mini-model 

### More Help
> For more help on downloading spaCy you can use [this GitHub repository](https://github.com/explosion/spaCy/issues/1721) for detailed documentation on how to deal with different issues.

## NLP Nitro Project

### UML Diagram - a brief overview

Feel free to scroll to view whole diagram or download by maximizing window

![NLP Nitro UML](https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro.png)

<div>
    <iframe src="https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro-UML.pdf&embedded=true" height="600" width="1000" allowfullscreen="" frameborder="0"></iframe>
</div>

[embed]https://github.com/bikegirl/CIT591-NLP-Nitro/blob/master/NLP-Nitro-UML.pdf[/embed]

### Main

Client Program calls complexifier GUI interface for the user.

### ComplexifierGUI Class

Serves as a graphical user interface between the User and implementation details of the program.  The class has 2 instance variables: called __application_window that displays the title for the TextWidget and __text_complexifier which is a TextComplifier object.

Methods include __complexify_and_display_text and run_complexifier_GUI.  __complexify_and_display_text will display the output vector un by run_complexifier_GUI.




