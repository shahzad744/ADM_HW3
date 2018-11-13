class Preprocessing:
    __tsvColumnFormat=["index","averageRateperNight","bedroomCount","city","dateofListing","description","latitude","longitude","title","url"]

    #this will take list of strings (strings of tsv files) and return with object with every column as key
    def __splitDataForTextManagement(self):
        pass
    #this will split search string for preprocessing
    def __splitDataForTextMining(self):
        pass
   #this will take list of strings and return list without stop words
    def __filterStopWords(self,data):
        return data
    #this will take list of strings and return list without punctuations
    def __filterPunctuations(self,data):
        return data
    #this will perform stemming on list of strings
    def __stemming(self,data):
        return data
    #this will take list of strings (strings of tsv files) an will process data 
    def PreprocessDataForTextManagement(self,listOftsv):

        data=__splitDataForTextManagement(self,listOftsv)
        for d in data:
            d["description"]=__filterStopWords(d["description"])
            d["title"]=__filterStopWords(d["title"])

            d["description"]=__filterPunctuations(d["description"])
            d["title"]=__filterPunctuations(d["title"])

            d["description"]=__stemming(d["description"])
            d["title"]=__stemming(data["title"])

        return data

    def PreprocessDataForTextMining(self,searchText):

        data=__splitDataForTextManagement(self,searchText)

        data=__filterStopWords(data)
        data=__filterPunctuations(data)
        data=__stemming(data)

        return data




