import readData as read
from learn import machines
from sklearn.metrics import accuracy_score

testLabel , trainLabel , testData , trainData = read.readData ()

machine = machines (testLabel , trainLabel , testData , trainData)

class Accuracy : 

    def __init__ (self, change) : 

        self.change = change
    
    def knnAccuracy (self) : 

        knnPredictions = machine.knn ()

        knnPrecision = accuracy_score (knnPredictions , testLabel) * 100

        print ("\n precisao do knn : " + str (knnPrecision) + " %")

    def decisionTreeAccuracy (self) :  

        decisionTreePredictions = machine.decisionTree () 

        decisionTreePrecision = accuracy_score (decisionTreePredictions , testLabel) * 100

        print ("\n precisao da arvore de decisao : " + str (decisionTreePrecision) + " %")

    def naiveBayesAccuracy (self) : 

        naiveBayesPredictions = machine.naiveBayes ()

        naiveBayesPrecision = accuracy_score (naiveBayesPredictions , testLabel) * 100

        print ("\n precisao do naive Bayes : " + str (naiveBayesPrecision) + " %")