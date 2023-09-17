import csv

class csvImporter():

    csvData = {}

    def __init__(self, csvFile):
        drinkId = 1
        with open(csvFile, 'r') as fd:
            reader = csv.DictReader(fd)  
            for row in reader:
                keepRow = True
                # Replace strings with integrers if possible
                for i, item in enumerate(row):
                    try:
                        row[item] = int(row[item])
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

    def getCsvDataDict(self):
        return dict(self.csvData)
        
