from collections import defaultdict

class TextManagement:
    """inverted index"""
    __resourcespath=".\\Resources"

    def CreateInvertedIndexFromData(self, data):
        """For a given list of objects representing tvs files,
        returns the inverted index."""
        inverted_index = defaultdict(list)
        for doc in data:
            terms = set()
            terms.update(doc["title"])
            terms.update(doc["description"])
            for t in terms:
                inverted_index[t].append(doc["index"])
        return inverted_index


    #saves the json of Inverted index object to the file in the resources folder
    def SaveInvertedIndexJson(self,data,filename):
        pass
    #load the json file from resources and return the object
    def LoadInvertedIndexJson(self,filename):
        pass




