import pandas
class DisplayResults:
    __simpleResultIndex=["Title","Description","City","Url"]
    __tsvpathFormat = ".\\Resources\\tsvFiles\\doc_{}.tsv"

    def PrintSimpleResults(self,documentIndexes):        
        data=[]
        for i in documentIndexes:
            tsv=self.__tsvpathFormat.format(i)
            with open(tsv,'r',encoding='utf-8') as f:
                content=f.read()
                contents=content.split('\t')
                wordsList=[contents[8],contents[5],contents[3],contents[9]]
                data.append(wordsList)

        if(len(data)==0):
            print("No records found.")
        else:
            df=pandas.DataFrame(data=data,columns=self.__simpleResultIndex)
            print(df)





