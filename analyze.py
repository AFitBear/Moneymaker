"""
Module where math happens. math and graphs.
"""
import matplotlib.pyplot as plt
import numpy as np

def graphlist(theList,endPoint,labelX=0,labelY=0, start=1,step=1):
    """
    takes a list and graphs it with given endpoint.
    """
    x = np.arange(start,endPoint,step)
    plt.plot(x,theList)
    if labelX!=0:plt.xlabel(labelX)
    if labelY!=0:plt.ylabel(labelY)
    plt.grid()
    plt.show()
    plt.savefig('graphOfFreezer.PNG')
    return True

def calc_cum_cost(freezertemp,pricelist,powerlist):
    """
    Calculates and returns the cumulative cost of a month, by adding electricity-cost and foodcost.
    >>> calc_cum_cost(analyze.calc_cum_cost([6,5,4],[1,2,3],[True,False,True]))
    4
    """
    cumcost=0
    for i in range(len(freezertemp)):#calcultes powercost, if the compressor was on it cost 1whr which is just 1 times the price
        if powerlist[i]:
            cumcost+=pricelist[i]
        cumcost+=calculateFoodCost(freezertemp[i])#calculates foodcost
    return cumcost

def calculateFoodCost(temp):
    """
    Calculates the food cost according to the temperature given.
    >>> calculateFoodCost(8)
    1.3135390859634013
    """
    if temp<3.5:#calculates foodcost
        foodCost=4.39*np.exp(-0.49*temp)
    elif temp>6.5:#calculates foodcost
        foodCost=0.11*np.exp(0.31*temp)
    else: return 0
    return foodCost

def calcTemp(lastTemp,c1,c2,tempKomp,tempRoom,deltaT):
    """
    Calculates the new temperature of the freezer.
    >>> calcTemp(6,(5*10**-7),(8*10**-6),-5,20,300)
    5.9757
    """
    return (lastTemp+(c1*(tempRoom-(lastTemp))+c2*(tempKomp-(lastTemp)))*deltaT)

if __name__== '__main__':
    import doctest
    print(doctest.testmod)