"""
Main, where it all begins.
"""
import pricelist
import freezer
import time
import analyze

"""
nowe=time.time()
print(freezer.simulateAverage(freezer.simulatesimplelist,1000,changePoint))
print(time.time()-nowe)
"""

changePoint=6.235
costlist=freezer.simulateAverage(freezer.simulatesimplelist,10,changePoint)
print(costlist)

startPoint=6.1
endPoint=6.4#it does not calculate the endpoint
step=0.01
costlist=freezer.pricePerTemp(10,startPoint,endPoint,step)
analyze.graphFreezerTemp(costlist,endPoint,'Skifte-Temperatur [C]','Udgifter [kr.]',start=startPoint,step=step)



#mindst 1 class, mindst 3 doctest, og doctekst til hver funktioner og moduler.
#mindst 2 moduler. budgettet er 12000
#TIL RAPPORT, testning af kølningstemperatur i forhold til "madkost vs elcost". Ved 5.9C er der 0 madkost og 6.2 er billiger end 5C.
#with physics it is best at 6.235[C] wher it changes.
if __name__== '__main__':
    import doctest
    print(doctest.testmod)