import csv
import os
class DataLoading:
    __csvpath = ".\\Resources\\Airbnb_Texas_Rentals.csv"
    __tsvpathFormat =".\\Resources\\tsvFiles\\doc_{}.tsv" 
    
    def LoadCSVandCreateTSVFiles(self):
        with open(self.__csvpath,'r',encoding='utf-8') as csvin:
            lines = csv.reader(csvin)
            for index,line in enumerate(lines):
                if(index == 0):
                    continue
                with open(self.__tsvpathFormat.format(index),'w',encoding='utf-8') as tsvout:
                    writer = csv.writer(tsvout, delimiter='\t')
                    writer.writerow(line)

     #this will return read all the tsv file in the given path and return list
     #of string in the tsv
    def LoadTSVFilesDataIntoString(self):
        pass
                





