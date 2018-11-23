import DataLoading
import Preprocessing
import TextManagement
import TextMining
import DisplayResults
dataloading = DataLoading.DataLoading()
preprocessing = Preprocessing.Preprocessing()
textManagement = TextManagement.TextManagement()
textMining = TextMining.TextMining()
displayresults=DisplayResults.DisplayResults()

lists = dataloading.LoadTSVFilesDataIntoString()
data = preprocessing.PreprocessDataForTextManagement(lists)
invertedIndex = textManagement.CreateInvertedIndexWithNewScore(data)
#save table maybe
textManagement.SaveInvertedIndexJson(invertedIndex, "table-custom-scored.json")
#load table from file
invertedIndex = textManagement.LoadInvertedIndexJson("table-custom-scored.json")
#Take search Query
print("Please Enter Search Query: ")
searchQuery = input()
searchQueryProcessed = preprocessing.PreprocessDataForTextMiningCustomScore(searchQuery)
documentIndexes = textMining.SearchTextFromInvertedCustomScoredIndexAndReturnResults(invertedIndex,searchQueryProcessed)

results=displayresults.GetScoredResults(documentIndexes)
print(results)



