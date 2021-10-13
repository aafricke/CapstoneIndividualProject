import csv
import pandas as pd

#get user's car make
def getMake():
    make = input("Enter desired car Make: (i.e. TESLA)")
    return(make)

#get user's range and check if exists
def getRange():
    crange = input("Enter minimum desired hours the car can drive before depletion: (i.e. 5)")

    df2 = pd.read_csv('range.csv')
    i = 1
    
   
    for row in df2:
        
        if int(df2.loc[i]) == int(crange):
            
            return(crange)

        else:
            print("That minimum value is not in range")
            getRange()
    

def customize():
    city = input("Would you like 'City (kWh/100 km)' included in the output? Type Yes or No: ")
    hwy = input("Would you like 'Hwy (kWh/100 km)' included in the output? Type Yes or No: ")
    distance = input("Would you like 'Distance (km)' included in the output? Type Yes or No: ")

    return city,hwy,distance

#create New CSV file with requested data
def createCSV(fileName,df3):
    f = open(fileName, "x")
    f.close()
    i = 0
    df3.to_csv(fileName, sep=",", index=False)
    
def search():
    column_name = ["make","model", "range(hr)"]
    df3 = pd.DataFrame(columns = column_name)
    
    df1 = pd.read_csv('cars.csv')

    userMake = getMake()
    userRange = getRang
    

    dfMake = df1["Make"]
    dfModel = df1["Model"]
    dfRange = df1["TIME (h)"]
    dfCity = df1["CITY (kWh/100 km)"]
    dfHwy = df1["HWY (kWh/100 km)"]
    dfDistance = df1["(km)"]
    

    city,hwy,distance = customize()


    i = 0
    
    for row in dfMake:
        
        carMake = dfMake[i]
        carRange = dfRange[i]
        
        if carMake == userMake and carRange >= int(userRange):
            df3.loc[i,"make"] = dfMake.loc[i]
            df3.loc[i,"model"] = dfModel.loc[i]
            df3.loc[i,"range(hr)"] = dfRange.loc[i]
            if city == "Yes":
                df3.loc[i,"City(kWh/100 km)"] = dfCity.loc[i]
            if hwy == "Yes":
                df3.loc[i,"Hwy(kWh/100 km)"] = dfCity.loc[i]
            if distance == "Yes":
                df3.loc[i,"Distance(km)"] = dfCity.loc[i]
        i += 1
        

    fName = input("Enter output file name: ") + ".csv"
    createCSV(fName,df3)

    final = pd.read_csv(fName)
  
    print("\n")

    print(final)

    main()

def edit():
    print("COMINGSOON")

def exitP():
    raise SystemExit
def main():

    function = input("Would you like to make a search or edit an existing file? Please type search, edit, or quit (ie. search)")

    if function == "search":
        search()
    elif function == "edit":
        edit()
    elif function == "quit":
        exitP()
    else:
        print(function + " is not a recognized function")
        main()

main()



