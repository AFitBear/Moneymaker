"""
Main
"""
import pricelist
import freezer
#freezer.simulate()
#freezer.simulatesimplelist()

freezer.pricePerTemp(4000)#000)

#for i in range(200):
#    freezer.simulatelist()
#freezer.pricePerTemp(4000)



#mindst 1 class, mindst 3 doctest, og doctekst til hver funktioner og moduler.
#mindst 2 moduler. budgettet er 12000
#TIL RAPPORT, testning af kølningstemperatur i forhold til "madkost vs elcost". Ved 5.9C er der 0 madkost og 62. er billiger end 5C.
#with physics it is best at 6.2[C] wher it changes.
if __name__== '__main__':
    import doctest
    print(doctest.testmod)