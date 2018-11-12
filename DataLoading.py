import csv
class DataLoading(object):
    __csvpath=".\\Resources\\Airbnb_Texas_Rentals.csv"
    __tsvpath=".\\Resources\\tsvFiles\\doc_{}.tsv"
    def LoadCSVandCreateTSVFiles():
        with open(__csvpath,'r',encoding='utf-8') as csvin:
            lines = csv.reader(csvin)
            for index,line in enumerate(lines):
                if(index==0):
                    continue
                with open(__tsvpath.format(index),'w',encoding='utf-8') as tsvout:
                    writer = csv.writer(tsvout, delimiter='\t')
                    writer.writerow(line)         





