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
                    docs=invertedTable[str(wordIndex)]
                    for doc in docs:
                        documentsSet.add(doc)
        return list(documentsSet)

