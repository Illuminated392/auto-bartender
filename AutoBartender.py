import sys, os

#local imports
import UserInterface
from DataImporter.CsvImporter import csvImporter 
#from DataStorage.<> import <>
#from ArduinoInterface.<> import <>


CATEGORIES = ["Vodka", "Gin", "Bourbon", "Light Rum", "Tequila"]
drinkClassDict = {}
drinkDict = {}
drinkLookupDict = {}

app = None

def loadDrinkClassDict(drinkDict):
    global drinkClassDict
    for cat in CATEGORIES:
        drinkClassDict[cat] = []

    for entry in drinkDict:
        try:
            cat = drinkDict[entry]["class"]
            drinkClassDict[cat].append(drinkDict[entry]["Drink"])
        except KeyError:
            print("Failed to get class or add entry to drink class dictionary")
            print(f"Entry: {entry} - Drink: {drinkDict[entry]['Drink']}")

def loadDrinkLookupDict(drinkDict):
    global drinkLookupDict
    for entry in drinkDict:
        key = drinkDict[entry]["Drink"]
        drinkLookupDict[key] = entry


def homeScreenCallback(selection):
    global app

    try:
        opts = drinkClassDict[selection]
    except KeyError:
        print(f"Invalid Selection: {selection}")
    
    app.DisplayMainOptionPage(selection, opts, drinkSelectionCallback, colCount=5)

def drinkSelectionCallback(drink):
    global app, drinkDict
    items = []
    values = []
    total = 0

    try:
        drinkId = drinkLookupDict[drink]
    except:
        print(f"Failed to find drink {drink}")
        app.DisplayHomePage(CATEGORIES, homeScreenCallback)
        return

    for item in drinkDict[drinkId]:
        if item == "Popularity Weight ( 1-10)":
            continue
        value = drinkDict[drinkId][item]
        if type(value) != str and value != 0:
            items.append(item)
            values.append(value)
             
    app.DisplayModificationPage(items, values, 20.0, orderCallback)


def orderCallback(modFrame):
    
    if modFrame != None:
        print(modFrame.getElementValues())
        #Get items from modframe
        #Submit order
    app.DisplayHomePage(CATEGORIES, homeScreenCallback)

def cancelOrderCallback():
    pass

def startupUI():    
    global app
    app = UserInterface.MainApp(orderCallback, CATEGORIES)

    app.DisplayHomePage(CATEGORIES, homeScreenCallback)
    
    app.mainloop()




def main():
    print("Running AutoBartender.py")
    
    global drinkDict

    importData = csvImporter("drinks_list_final.csv", CATEGORIES)

    drinkDict = importData.getCsvDataDict()

    loadDrinkClassDict(drinkDict)
    loadDrinkLookupDict(drinkDict)

    startupUI()

    #dbClass = databaseStorage(drinkDict)
    




if __name__=="__main__":
    main()
