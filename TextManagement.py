from collections import defaultdict
import json

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

    def SaveInvertedIndexJson(self, data, filename):
        """saves the json of Inverted index object to the file"""
        with open(filename, 'w') as f:
            json.dump(data, f)

    def LoadInvertedIndexJson(self, filename):
        """load the json file from file and return the object"""
        with open(filename, 'r') as f:
            inverted_index = json.load(f)
        return inverted_index




