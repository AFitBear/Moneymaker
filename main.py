"""
Main
"""
import pricelist
import freezer
import time
#freezer.simulate()
changePoint=6.24
#print(freezer.simulatesimplelist(changePoint))
#print(freezer.simulateAI(600,1))

#print(freezer.simulateAverage(freezer.simulatesimplelist,1000,changePoint))

"""
nowe=time.time()
print(freezer.simulateAverage(freezer.simulatesimplelist,1000,changePoint))
print(time.time()-nowe)
"""
startPoint=6.247
endPoint=6.253
step=0.002
freezer.pricePerTemp(30000,startPoint,endPoint,step)


#for i in range(200):
#    freezer.simulatelist()
#freezer.pricePerTemp(4000)



#mindst 1 class, mindst 3 doctest, og doctekst til hver funktioner og moduler.
#mindst 2 moduler. budgettet er 12000
#TIL RAPPORT, testning af kølningstemperatur i forhold til "madkost vs elcost". Ved 5.9C er der 0 madkost og 62. er billiger end 5C.
#with physics it is best at 6.22[C] wher it changes.
if __name__== '__main__':
    import doctest
    print(doctest.testmod)