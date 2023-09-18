from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

class machines : 

    def __init__ (self , testLabel , trainLabel , testData , trainData) : 
 
        self.testLabel = testLabel
        self.trainLabel = trainLabel
        self.testData = testData
        self.trainData = trainData

    def knn (self) : 

        knn = KNeighborsClassifier (n_neighbors = 11 , algorithm = "kd_tree" , n_jobs = - 1)

        knn.fit (self.trainData , self.trainLabel)

        testPrediction = knn.predict (self.testData)

        return testPrediction
    
    def decisionTree (self) : 

        decisionTree = DecisionTreeClassifier (splitter = "best" , random_state = 30)
        
        decisionTree.fit (self.trainData , self.trainLabel)

        testPrediction = decisionTree.predict (self.testData)

        return testPrediction
    
    def naiveBayes (self) : 

        naiveBayes = GaussianNB ()

        naiveBayes.fit (self.trainData , self.trainLabel)

        testPrediction = naiveBayes.predict (self.testData)

        return testPrediction
