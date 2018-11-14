import DataLoading
import Preprocessing
import TextManagement
import TextMining

dataloading = DataLoading.DataLoading()
preprocessing = Preprocessing.Preprocessing()
textManagement = TextManagement.TextManagement()
textMining = TextMining.TextMining()

lists = dataloading.LoadTSVFilesDataIntoString()
data = preprocessing.PreprocessDataForTextManagement(lists)
invertedIndex = textManagement.CreateInvertedIndexFromData(data)
#save table maybe
textManagement.SaveInvertedIndexJson(invertedIndex, "table.json")
#load table from file
invertedIndex = textManagement.LoadInvertedIndexJson("table.json")
#Take search Query
print("Please Enter Search Query: ")
searchQuery = input()
searchQueryProcessed = preprocessing.PreprocessDataForTextMining(searchQuery)
results = textMining.SearchTextFromInvertedIndexAndReturnResults(invertedIndex,searchQueryProcessed)

print(results)



