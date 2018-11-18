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
invertedIndex = textManagement.CreateScoredInvertedIndex(data)
#save table maybe
textManagement.SaveInvertedIndexJson(invertedIndex, "table-scored.json")
#load table from file
invertedIndex = textManagement.LoadInvertedIndexJson("table-scored.json")
#Take search Query
print("Please Enter Search Query: ")
searchQuery = input()
searchQueryProcessed = preprocessing.PreprocessDataForTextMining(searchQuery)
documentIndexes = textMining.SearchTextFromInvertedScoredIndexAndReturnResults(invertedIndex,searchQueryProcessed)

displayresults.PrintScoredResults(documentIndexes)



