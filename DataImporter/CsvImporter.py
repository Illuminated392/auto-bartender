import csv

class csvImporter():

    csvData = {}

    def __init__(self, csvFile, categories=None):
        drinkId = 1
        with open(csvFile, 'r') as fd:
            reader = csv.DictReader(fd)  
            for row in reader:
                keepRow = True
                # Replace strings with integers if possible
                for i, item in enumerate(row):
                    try:
                        row[item] = float(row[item])
                    except ValueError:
                        # Swap empty string with value of zero
                        if row[item] == '':
                            row[item] = 0
                    if i == 0:
                        keepRow = False if row[item] == 0 else True
                        if not keepRow:
                            break
                if keepRow:
                    self.csvData[drinkId] = row
                drinkId += 1

        self.categorizeData(categories)

    def categorizeData(self, categories): 
        if categories == None:
            return
        
        for entry in self.csvData:
            index = -1
            maxValue = -1
            for i, cat in enumerate(categories):
                try:
                    if self.csvData[entry][cat] > maxValue:
                        maxValue = self.csvData[entry][cat]
                        index = i
                except KeyError:
                    print(f"Category {cat} does not exist for {entry}")
            if index >= 0:
                self.csvData[entry]["class"] = categories[index]
            else:
                self.csvData[entry]["class"] = "Misc"

    def getCsvDataDict(self):
        return dict(self.csvData)
        
