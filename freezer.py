"""
Module where the freezer operates and the logic of the freezer is executed.
"""
import random
import analyze
from pricelist import get_price_list
import numpy as np

class Freezerroom:
    """class that have basic data of the freezer"""
    def __init__(self):
            self.deltaT=300
            self.komptemp=-5
            self.roomtemp=20.0
            self.pricelist=get_price_list()

def simulatesimplelist(changepoint):
    """simulates 1 month of a simple freezer/thermostat, with one given changepoint and returns the cumulative cost."""
    freezer=Freezerroom()
    powerlist=np.array([False]*len(freezer.pricelist))
    freezertemp=np.array([0.0]*(len(freezer.pricelist)+1))
    freezertemp[0]=5.0

    for i in range(len(freezertemp)-1):#logic for if the door opens
        if random.randint(1,10)==1:
            c1=3*10**-5
        else:                             #make new funktion that checks the food cost/price.
            c1=5*10**-7
        if freezertemp[i]>changepoint:#logic to se if the tempereture is over 5, if it is, then it cools down.
            c2=8*10**-6
            powerlist[i]=True
        else:
            c2=0
        freezertemp[i+1]=analyze.calcTemp(freezertemp[i],c1,c2,freezer.komptemp,freezer.roomtemp,freezer.deltaT)
    cumcost=analyze.calc_cum_cost(np.delete(freezertemp,-1),freezer.pricelist,powerlist)
    return cumcost

def simulateAverage(funktion,cylces,changePoint):
    """
    Simulates a funktion/freezer a given times(cycles) and returns the average cost.
    """
    cumsum=0
    for i in range(cylces):
        cumsum+=funktion(changePoint)
    avg=cumsum/cylces
    return avg

def pricePerTemp(cycles,startPoint,endPoint,step):
    """
    gives a list of the average cost of each changepoint, with a given startpoint, endpoint and steps between each changepoints. 
    """
    points=np.arange(startPoint,endPoint,step)
    costlist=[0]*len(points)
    i=0
    for temp in points:
        costlist[i]=simulateAverage(simulatesimplelist,cycles,temp)
        i+=1
        print(f"procent af cycle: {(i/len(points))*100}")
    return costlist
