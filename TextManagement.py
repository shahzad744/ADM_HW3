from collections import defaultdict
import json
import WordsDictionary
import math

class TextManagement:
    """inverted index"""
    __resourcespath=".\\Resources"

    def CreateInvertedIndex(self, data):
        """For a given list of objects representing tvs files,
        returns the inverted index."""
        vocab = WordsDictionary.WordsDictionary()
        inverted_index = defaultdict(list)
        for doc in data:
            terms = set()
            terms.update(doc["title"])
            terms.update(doc["description"])
            for t in terms:
                if vocab.HasWordInDictionary(t):
                    inverted_index[vocab.GetTermIdByWord(t)].append(doc["index"])
                
        return inverted_index

    def CreateScoredInvertedIndex(self,data):
        """For a given list of objects representing tvs files,
                returns the scored (tf*idf) inverted index."""
        vocab = WordsDictionary.WordsDictionary()
        inverted_index = defaultdict(list)
        collection_distinct_terms = set()
        for doc in data:
            terms = list()
            terms += doc["title"]
            terms += doc["description"]

            distinct_terms = set(terms)
            for t in distinct_terms:
                if vocab.HasWordInDictionary(t):
                    tf = terms.count(t)
                    inverted_index[vocab.GetTermIdByWord(t)].append((doc["index"], tf))
            collection_distinct_terms.update(distinct_terms)
        # compute idf(s)
        idfs = {}
        for t in collection_distinct_terms:
            if vocab.HasWordInDictionary(t):
                word_id = vocab.GetTermIdByWord(t)
                idfs[word_id] = math.log2(len(data) / len(inverted_index[word_id]))
        # update the index
        for wid in idfs:
            post_list = inverted_index[wid]
            idf = idfs[wid]
            inverted_index[wid] = list(map(lambda p: (p[0], p[1]*idf), post_list))
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




