import csv
import pandas as pd

def getMake():
    make = input("Enter desired car Make: (i.e. TESLA)")
    return(make)

def getRange():
    crange = input("Enter minimum desired hours the car can drive before depletion: (i.e. 5)")
    return(crange)

def createCSV(fileName,df3):
    f = open(fileName, "x")
    f.close()
    i = 0
    df3.to_csv(fileName, sep=",", index=False)

    

def search():
    column_name = ["make", "range(hr)"]
    df3 = pd.DataFrame(columns = column_name)
    
    df1 = pd.read_csv('cars.csv')
    df2 = pd.read_csv('range.csv')

    userMake = getMake()
    userRange = getRange()
    
    i = 0

    dfMake = df1["Make"]
    dfRange = df1["TIME (h)"]
    
    for row in dfMake:
        
        carMake = dfMake[i]
        carRange = dfRange[i]
        
        if carMake == userMake and carRange == int(userRange):
            df3.loc[i] = dfMake.loc[i]
            df3.loc[i,"range(hr)"] = dfRange.loc[i]
        i += 1
        

    fName = input("Enter output file name: ") + ".csv"
    createCSV(fName,df3)
  
    print("\n")

    final = pd.read_csv(fName)

    print(final)

search()



