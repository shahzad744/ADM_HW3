import WordsDictionary
import heapq
import math
from collections import defaultdict
class TextMining:
    __k=20

    def __calculateCosineSimilarity(self,listOfScores):
        sum=0
        squaredsum=0
        for scores in listOfScores:
            sum+=scores
            squaredsum+= scores*scores
        val=sum/math.sqrt(squaredsum)
        return val/len(listOfScores)
    #it takes inverted table and search query and perform text mining on
    #inverted table and return list of search results
    def SearchTextFromInvertedIndexAndReturnResults(self,invertedTable,searchText):
        listOfDocs=[]
        vocab=WordsDictionary.WordsDictionary()
        for searchWord in searchText:
            if(vocab.HasWordInDictionary(searchWord)):
                wordIndex=vocab.GetTermIdByWord(searchWord)
                if(str(wordIndex) in invertedTable):
                    docs=set(invertedTable[str(wordIndex)])
                    listOfDocs.append(docs)
                else:
                    return []
        return list(set.intersection(*listOfDocs))

    def SearchTextFromInvertedScoredIndexAndReturnResults(self,invertedScoredTable,searchText):
        listOfDocs=[]
        documentListWithScores=[]
        documentListWithScoresSorted=[]
        vocab=WordsDictionary.WordsDictionary()
        termScores=defaultdict(list)        
        for searchWord in searchText:
            if(vocab.HasWordInDictionary(searchWord)):
                wordIndex=vocab.GetTermIdByWord(searchWord)
                if(str(wordIndex) in invertedScoredTable):
                    docs=invertedScoredTable[str(wordIndex)]
                    docsSet=set()
                    for doc in docs:
                        docsSet.add(doc[0])
                        termScores[doc[0]].append(doc[1])
                    listOfDocs.append(docsSet)
                else:
                    return []

        listOfDocs=list(set.intersection(*listOfDocs))
        for dd in listOfDocs:
            heapq.heappush(documentListWithScores,(1-self.__calculateCosineSimilarity(termScores[dd]),dd))
        i=0
        while i <self.__k and i<len(documentListWithScores):
            temp=heapq.heappop(documentListWithScores)
            documentListWithScoresSorted.append((temp[1],1-temp[0]))
            i+=1

        return documentListWithScoresSorted


