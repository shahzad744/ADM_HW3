import csv
import os
from pathlib import Path


class DataLoading:
    __csvpath = ".\\Resources\\Airbnb_Texas_Rentals.csv"
    __tsvpathFormat = ".\\Resources\\tsvFiles\\doc_{}.tsv"
    __tsvDir = "./Resources/tsvFiles"
    
    def LoadCSVandCreateTSVFiles(self):
        with open(self.__csvpath,'r',encoding='utf-8') as csvin:
            lines = csv.reader(csvin)
            for index,line in enumerate(lines):
                if(index == 0):
                    continue
                with open(self.__tsvpathFormat.format(index),'w',encoding='utf-8') as tsvout:
                    writer = csv.writer(tsvout, delimiter='\t')
                    writer.writerow(line)

    def LoadTSVFilesDataIntoString(self):
        """Returns a list of strings, each containing the content of tsv file"""
        path = Path(self.__tsvDir)
        tsv = list(path.glob('*.tsv'))
        data = []
        for p in tsv:
            with open(p) as f:
                data.append(f.read())
        return data


