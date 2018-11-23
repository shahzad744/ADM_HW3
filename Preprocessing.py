from nltk.corpus import stopwords
import string as stri
import re
from datetime import datetime
from nltk.stem.snowball import EnglishStemmer


class Preprocessing:
    __tsvColumnFormat = ["index", "averageRateperNight", "bedroomCount", "city", "dateofListing", "description",
                         "latitude", "longitude", "title", "url"]

    def __splitDataForTextManagement(self, strings):
        """For a given list of strings, each containing the content of a tvs file,
        returns a list of objects representing the tvs files. These objects are dictionaries
        where the keys are the names of the fields."""
        structured_data = []
        for string in strings:
            content = dict()
            for i, split in enumerate(string.lower().split("\t")):
                if i == 0:
                    content[self.__tsvColumnFormat[i]] = int(split)
                elif i == 1:
                    if not split:
                        content[self.__tsvColumnFormat[i]]=0
                    else:
                        content[self.__tsvColumnFormat[i]] = int(split[1:])

                elif i == 2:
                    if not split or split=="studio":
                        content[self.__tsvColumnFormat[i]]=0
                    else:
                        content[self.__tsvColumnFormat[i]] = int(split)
                elif i==3 or i==9:
                    content[self.__tsvColumnFormat[i]] = str(split)
                elif i==4:
                    content[self.__tsvColumnFormat[i]]=datetime.strptime(split,"%B %Y")
                elif i==6 or i==7:
                    if split=="na":
                        content[self.__tsvColumnFormat[i]]=0.0
                    else:
                        content[self.__tsvColumnFormat[i]] = float(split)
                else:
                    content[self.__tsvColumnFormat[i]] = split.split(' ')
            structured_data.append(content)
        return structured_data

    # this will split search string for preprocessing
    def __splitDataForTextMining(self,string):
        return string.lower().split(" ")
    def __splitDataForTextMiningCustomScore(self,string):
        dic=dict()
        numbers = re.findall('\d+',string)
        numbers = list(map(int,numbers))
        dic["Numbers"]=numbers
        dic["Words"]=string.lower().split(" ")
        return dic

    # this will take list of strings and return list without stop words
    def __filterStopWords(self, data):
        stop_words = set(stopwords.words("english"))
        filtered = []
        for word in data:
            if word not in stop_words:
                filtered.append(word)
        return filtered

    # this will take list of strings and return list without punctuations
    def __filterPunctuations(self, data):
        remove_punct = str.maketrans('', '', stri.punctuation + '“”–’')
        filtered = []
        for word in data:
            filtered.append(word.translate(remove_punct))
        return filtered

    # this will perform stemming on list of strings
    def __stemming(self, data):
        stemmer = EnglishStemmer()
        filtered = []
        for word in data:
            filtered.append(stemmer.stem(word))
        return filtered

    # this will take list of strings (strings of tsv files) an will process data
    def PreprocessDataForTextManagement(self, listOftsv):
        data = self.__splitDataForTextManagement(listOftsv)
        for d in data:
            d["description"] = self.__filterStopWords(d["description"])
            d["title"] = self.__filterStopWords(d["title"])

            d["description"] = self.__filterPunctuations(d["description"])
            d["title"] = self.__filterPunctuations(d["title"])

            d["description"] = self.__stemming(d["description"])
            d["title"] = self.__stemming(d["title"])

        return data

    def PreprocessDataForTextMining(self, searchText):

        data = self.__splitDataForTextMining(searchText)

        data = self.__filterStopWords(data)
        data = self.__filterPunctuations(data)
        data = self.__stemming(data)

        return data
    def PreprocessDataForTextMiningCustomScore(self, searchText):

        data = self.__splitDataForTextMiningCustomScore(searchText)
        data["Words"] = self.__filterStopWords(data["Words"])
        data["Words"] = self.__filterPunctuations(data["Words"])
        data["Words"] = self.__stemming(data["Words"])

        return data
