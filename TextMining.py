import WordsDictionary
import heapq
import math
import datetime
from collections import defaultdict


class TextMining:
    __k=100      

    def __calculateCosineSimilarity(self,listOfScores,queryscoreList):
        sum=0
        squaredsumA=0
        squaredsumB=0
        for i in range(0,len(queryscoreList)):
            sum+=listOfScores[i]*queryscoreList[i]
            squaredsumA+= listOfScores[i]*listOfScores[i]
            squaredsumB+= queryscoreList[i]*queryscoreList[i]
        val=sum/(math.sqrt(squaredsumA)*math.sqrt(squaredsumB))
        return val
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
    def __calculateCustomScore(self,searchText,docDetailDic):
        roomno=[]
        price=[]
        priceweight=0
        bedroomweight=0
        cityweight=200
        now=datetime.datetime.now()
        publishDate=datetime.datetime.strptime(docDetailDic[4],"%Y-%m-%d %H:%M:%S")
        dateDiffweight=(now - publishDate).days
        if docDetailDic[3] in searchText["Words"]:
            cityweight=0
        numbers=searchText["Numbers"];
        for num in numbers:
            if(num>=0 and num<=15):
                roomno.append(num)
            if(num>15):
                price.append(num)

        if(len(roomno)>0):
            r=sum(roomno)/len(roomno)
            bedroomweight= 10*abs(r-docDetailDic[1])

        if(len(price)>0):
            r=sum(price)/len(price)
            priceweight= abs(r-docDetailDic[0])

        return (15300-priceweight-bedroomweight-cityweight-dateDiffweight)/15300
    def SearchTextFromInvertedCustomScoredIndexAndReturnResults(self,invertedTable,searchText):
        listOfDocs=[]
        documentListWithScores=[]
        documentListWithScoresSorted=[]
        docDetailDic=dict()
        vocab=WordsDictionary.WordsDictionary()
        for searchWord in searchText["Words"]:
            if(vocab.HasWordInDictionary(searchWord)):
                wordIndex=vocab.GetTermIdByWord(searchWord)
                if(str(wordIndex) in invertedTable):
                    docs=list(invertedTable[str(wordIndex)])
                    for doc in docs:
                        listOfDocs.append(doc[0])
                        docDetailDic[doc[0]]=doc
                else:
                    return []
        allDocs= list(set(listOfDocs))
        for dd in allDocs:
            heapq.heappush(documentListWithScores,(1-self.__calculateCustomScore(searchText,docDetailDic[dd]),dd))
        
        i=0
        while i <self.__k and i<len(documentListWithScores):
            temp=heapq.heappop(documentListWithScores)
            documentListWithScoresSorted.append((temp[1],1-temp[0]))
            i+=1

        return documentListWithScoresSorted


    def SearchTextFromInvertedScoredIndexAndReturnResults(self,invertedScoredTable,searchText):
        listOfDocs=[]
        documentListWithScores=[]
        documentListWithScoresSorted=[]
        vocab=WordsDictionary.WordsDictionary()
        termScores=defaultdict(list)  
        totalDocuments=set()
        vals=list(invertedScoredTable.values())
        for i in vals:
            for j in i:
                totalDocuments.add(j[0])
        querytermScores=[]
        for searchWord in searchText:
            if(vocab.HasWordInDictionary(searchWord)):
                wordIndex=vocab.GetTermIdByWord(searchWord)
                if(str(wordIndex) in invertedScoredTable):
                    docs=invertedScoredTable[str(wordIndex)]
                    docsSet=set()
                    tf=searchText.count(searchWord)/len(searchText)
                    idf=math.log2(len(totalDocuments)/len(docs))
                    querytermScores.append(tf*idf)
                    for doc in docs:
                        docsSet.add(doc[0])
                        termScores[doc[0]].append(doc[1])
                    listOfDocs.append(docsSet)
                else:
                    return []

        listOfDocs=list(set.intersection(*listOfDocs))
        for dd in listOfDocs:
            heapq.heappush(documentListWithScores,(1-self.__calculateCosineSimilarity(termScores[dd],querytermScores),dd))
        i=0
        while i <self.__k and i<len(documentListWithScores):
            temp=heapq.heappop(documentListWithScores)
            documentListWithScoresSorted.append((temp[1],1-temp[0]))
            i+=1

        return documentListWithScoresSorted


