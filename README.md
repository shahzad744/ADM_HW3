# Homework 3 - Find the perfect place to stay in Texas!

## Resources folder

This folder conatins:

* Airbnb_Texas_Rentals.csv: the given dataset
* words.txt: the vocabulary used to create the inverted index
* tsvFiles: this folder contains .tsv files, each corresponding to a row in the given dataset

## Python modules/files

* DataLoading.py: contains the class DataLoading that is responsible to create the .tsv files and ( D: ) load them in memory.
* DisplayResults.py: contains the class DisplayResult that is responsible to format the result of a query execution in a human-readble way
* Preprocessing.py: contains the class Preprocessing. Its responsibility is to preprocess the text-data using stepword and punctuation removal, and stemming.
* TextManagement.py: contains the class TextManagement that is responsible to manage the inverted index.
* TextMining.py: contains the class TextMining. Its responsiblity is to execute a query.
* WordDictionary.py: contains the class WordDictionary that manages the dictionary.
