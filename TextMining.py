import WordsDictionary
class TextMining:

    #it takes inverted table and search query and perform text mining on
    #inverted table and return list of search results
    def SearchTextFromInvertedIndexAndReturnResults(self,invertedTable,searchText):
        documentsSet=set()
        vocab=WordsDictionary.WordsDictionary()
        for searchWord in searchText:
            if(vocab.HasWordInDictionary(searchWord)):
                wordIndex=vocab.GetTermIdByWord(searchWord)
                if(str(wordIndex) in invertedTable):
                    docs=set(invertedTable[str(wordIndex)])
                    if(len(documentsSet)==0):
                        documentsSet=docs
                    else:
                        documentsSet=documentsSet.intersection(docs)                    
        return list(documentsSet)

    def SearchTextFromInvertedScoredIndexAndReturnResults(self,invertedScoredTable,searchText):
        pass

