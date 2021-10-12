import pandas as pd

def getMake():
    make = input("Enter desired car Make: (i.e. Tesla)")
    return(make)
    


def createCSV():
    column_name = ["make", "range(hr)"]
    df3 = pd.DataFrame(columns = column_name)
    
    df1 = pd.read_csv('cars.csv')
    df2 = pd.read_csv('range.csv')

    userMake = getMake()
    
    i = 0

    dfMake = df1["Make"]
    for row in dfMake:
        
        careMake = dfMake[i]
        if careMake == userMake :
            df3.loc[i] = dfMake.loc[i]
        i += 1

    print("\n")
    print(df3)
        

