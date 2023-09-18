import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize

def readData () : 

    allData = p.read_csv ("transfer.csv")

    trainData, testData = train_test_split (allData , test_size = 0.5 , random_state = 30000 , shuffle = True)

    trainLabel = trainData ["fraud"]
    del trainData ["fraud"]

    testLabel = testData ["fraud"]
    del testData ["fraud"]

    trainData = normalize (trainData , axis = 0)
    testData = normalize (testData , axis = 0)

    return testLabel , trainLabel , testData , trainData 