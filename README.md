# CIT591-NLP-Nitro
CIT 591 End of the Year Project

## Introduction

Our project would not be possible without the contributions of NAACL paper [Simple PPDB contextual simplification] (http://cis.upenn.edu/~ccb/publications/simple-ppdb.pdf).  As an extension to prior work completed by [Reno Kris](https://rekriz11.github.io/), NLP Nitro aims to implement this research paper backwards and transform any content message into a higher complexity score ("Shakespearify" any text, if you will).

## Depedencies

- In your python environment, you must install spaCy by going to [spaCy website: linguistic features documentation](https://spacy.io/usage/linguistic-features).  
- Although this should work with anything higher than **python 2.6**, we recommend **python 3** for running this project (I used Python 3.6 and my partner uses Python 3.5).  

## Downloading spaCey
- `import spaCy`
- Change directory be in working project folder
- use `pip install -U spacy && python -m spacy download en`

## Common Errors
1. the encoding for reading in a file.  Be sure to encode with UTF-8.  If you get an error that says something to the effect of "not recognizing ASCII characters," this is why. 
2. Project interpreters in your IDE (i.e. - PyCharm, Spyder).  Ensure you cd to the working directory of your project in command line.  Once you've set the right directory in command line run "python" to ensure you are using python 2.6 or higher.  If it turns out you are not running the correct Python, you must download at this time.
3. Path not found, file not found.  This means although you many have downloaded spaCy, you did not download it to the interpreter you thought you did.  You select correct python for your interpreter and then see (2) as reference.  Switch to working directly, verify which Python is being linked to the working directory, if not correct Python download accordingly. 
4. Cannot fine module en or couldn't link model.  You must use a seperate command to download the English model, try these two version b/c it depends on an individual basis how you set up your environment and where the pathway to your python download is located:
  1. `nlp = spacy.load('en_core_web_sm')`
  2. `nlp = spacy.load('en_core_web_sm')`
