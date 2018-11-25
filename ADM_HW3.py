import DataLoading
import Preprocessing
import TextManagement
import TextMining
import DisplayResults
import MapDrawer
from geopy import distance
import folium

def BonusTask():
    print("Enter comma seperated Cordinates:")
    cc=input()
    cor=(float(cc.split(",")[0]),float(cc.split(",")[1]))
    print("Distance in km: ")
    dis=float(input())
    dataloading = DataLoading.DataLoading()
    lists = dataloading.LoadTSVFilesDataIntoString()
    docIncluded=[]
    for rec in lists:
        rec=rec.split("\t")
        if(rec[6]=="NA" or rec[7]=="NA"):
            continue
        docCor=(float(rec[6]),float(rec[7]))
        if(distance.distance(cor,docCor).km<=dis):
            docIncluded.append([float(rec[6]),float(rec[7]),rec[8],rec[9]])
    m = folium.Map(location=cor)
    folium.Circle(
    location=cor,
    radius=dis*1000,
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
    ).add_to(m)
    folium.Marker(
    location=cor,
    tooltip='You are here!',
    icon=folium.Icon(color='green')
    ).add_to(m)
    for rec in docIncluded:
        folium.Marker(
        location=[rec[0],rec[1]],
        tooltip=rec[2],
        popup=rec[3],
        icon=folium.Icon(color='blue')
        ).add_to(m)
    m.save('index.html')


print("Enter comma seperated Cordinates:")
cc = input()
cor = (float(cc.split(",")[0]), float(cc.split(",")[1]))
print("Distance in km: ")
dis = float(input())

md = MapDrawer.MapDrawer(cor, dis)
md.draw()

#dataloading = DataLoading.DataLoading()
#preprocessing = Preprocessing.Preprocessing()
#textManagement = TextManagement.TextManagement()
#textMining = TextMining.TextMining()
#displayresults=DisplayResults.DisplayResults()

#lists = dataloading.LoadTSVFilesDataIntoString()
#data = preprocessing.PreprocessDataForTextManagement(lists)
#invertedIndex = textManagement.CreateInvertedIndexWithNewScore(data)
##save table maybe
#textManagement.SaveInvertedIndexJson(invertedIndex, "table-custom-scored.json")
##load table from file
#invertedIndex = textManagement.LoadInvertedIndexJson("table-custom-scored.json")
##Take search Query
#print("Please Enter Search Query: ")
#searchQuery = input()
#searchQueryProcessed = preprocessing.PreprocessDataForTextMiningCustomScore(searchQuery)
#documentIndexes = textMining.SearchTextFromInvertedCustomScoredIndexAndReturnResults(invertedIndex,searchQueryProcessed)

#results=displayresults.GetScoredResults(documentIndexes)
#print(results)





