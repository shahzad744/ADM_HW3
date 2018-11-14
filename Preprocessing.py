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
            for i, split in enumerate(string.split("\t")):
                if i == 0:
                    content[self.__tsvColumnFormat[i]] = int(split)
                else:
                    content[self.__tsvColumnFormat[i]] = split.split(' ')
            structured_data.append(content)
        return structured_data

    # this will split search string for preprocessing
    def __splitDataForTextMining(self):
        pass

    # this will take list of strings and return list without stop words
    def __filterStopWords(self, data):
        return data

    # this will take list of strings and return list without punctuations
    def __filterPunctuations(self, data):
        return data

    # this will perform stemming on list of strings
    def __stemming(self, data):
        return data

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

        data = __splitDataForTextManagement(self, searchText)

        data = __filterStopWords(data)
        data = __filterPunctuations(data)
        data = __stemming(data)

        return data
