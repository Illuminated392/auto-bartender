import sys, os

#local imports
import UserInterface
from DataImporter.CsvImporter import csvImporter 
#from DataStorage.<> import <>
#from ArduinoInterface.<> import <>



def main():
    print("Running AutoBartender.py")
    
    importData = csvImporter("drinks_list_final.csv")

    print(importData.getCsvDataDict())


if __name__=="__main__":
    main()
