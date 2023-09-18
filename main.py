from accuracy import Accuracy
import time

change = int (input ("qual inteligência vai querer ? \n \n 1 - knn \n 2 - arvore de decisao \n 3 - naive Bayes \n 4 - todos \n 5 - sair \n opcao : "))

accuracy = Accuracy (change)

if change == 1 : 
    
    start = time.time ()

    accuracy.knnAccuracy ()

    end = time.time ()

    timer = end - start

    print ("\n tempo : " + str (timer) + " s")

elif change == 2 : 

    start = time.time ()

    accuracy.decisionTreeAccuracy ()

    end = time.time ()

    timer = end - start

    print ("\n tempo : " + str (timer) + " s")

elif change == 3 : 

    start = time.time ()

    accuracy.naiveBayesAccuracy ()

    end = time.time ()

    timer = end - start

    print ("tempo : " + str (timer) + " s")

elif change == 4 : 

    start = time.time ()

    accuracy.knnAccuracy ()
    accuracy.decisionTreeAccuracy ()
    accuracy.naiveBayesAccuracy ()

    end = time.time ()

    timer = end - start

    print ("\n tempo : " + str (timer) + " s")

elif change == 5: 

    print ("\n algoritmo finalizado")

else : 

    print ("\n opcao inexistente, algoritmo finalizado")