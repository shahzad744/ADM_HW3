import pandas


class DisplayResults:
    __simpleResultIndex=["Title","Description","City","Url"]
    __scoredResultIndex=["Title","Description","City","Url","Score"]
    __tsvpathFormat = "./Resources/tsvFiles/doc_{}.tsv"

    def GetSimpleResults(self,documentIndexes):
        data=[]
        for i in documentIndexes:
            tsv=self.__tsvpathFormat.format(i)
            with open(tsv,'r',encoding='utf-8') as f:
                content=f.read()
                contents=content.split('\t')
                wordsList=[contents[8],contents[5],contents[3],contents[9]]
                data.append(wordsList)

        if(len(data)==0):
            return pandas.DataFrame(data="No records found.")
        else:
            return pandas.DataFrame(data=data,columns=self.__simpleResultIndex)

    def GetScoredResults(self,documentIndexes):
        data=[]
        for i in documentIndexes:
            tsv=self.__tsvpathFormat.format(i[0])
            with open(tsv,'r',encoding='utf-8') as f:
                content=f.read()
                contents=content.split('\t')
                wordsList=[contents[8],contents[5],contents[3],contents[9],i[1]]
                data.append(wordsList)

        if(len(data)==0):
            return pandas.DataFrame(data="No records found.")
        else:
            return pandas.DataFrame(data=data,columns=self.__scoredResultIndex)





