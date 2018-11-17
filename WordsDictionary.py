class WordsDictionary:
    __wordsTextFilePath="./Resources/words.txt"
    __wordsDictionary=dict()
    __wordsInvertedDictionary=dict()
    def __init__(self):
        with open(self.__wordsTextFilePath,'r',encoding='utf-8') as csvin:
            count=0
            fp=csvin.readline()
            while(fp):                
                self.__wordsDictionary[str(count)]=fp.rstrip().lower()
                self.__wordsInvertedDictionary[fp.rstrip().lower()]=count
                fp=csvin.readline()
                count+=1

    def GetTermIdByWord(self,word):
        return self.__wordsInvertedDictionary[word]

    def HasWordInDictionary(self,word):
        if (word in self.__wordsInvertedDictionary):
            return True
        return False

    def GetWordByTermId(self,termId):
        return self.__wordsDictionary[termId]

