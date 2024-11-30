import random
import data
import analyze
from pricelist import get_price_list
import numpy as np
#import analyze

"""
class Freezer:
    __builtins__
"""

def simulatesimplelist(changepoint):
    pricelist=get_price_list()
    powerlist=np.array([False]*len(pricelist))
    freezertemp=np.array([0.0]*(len(pricelist)+1))
    freezertemp[0]=5.0
    roomtemp=20.0
    komptemp=-5
    deltat=300
    #power=1
    c1=3*10**-5
    c2=8*10**-6
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
        freezertemp[i+1]=calcTemp(freezertemp[i],c1,c2,komptemp,roomtemp,deltat)
    
    #freezertemp.pop()
    #analyze.graphFreezerTemp(freezertemp) #makes a graph of the temperature
    cumcost=analyze.calc_cum_cost(freezertemp,pricelist,powerlist)
    return cumcost




"""
def simulateAIlist(t_point):
    pricelist=get_price_list()
    powerlist=[False]*len(pricelist)
    freezertemp=[0.0]*(len(pricelist)+1-stop_at_number)
    freezertemp[0]=5.0
    roomtemp=20.0
    komptemp=-5
    deltat=300
    #power=1
    c1=3*10**-5
    c2=8*10**-6
    for i in range(len(freezertemp)-1):#logic for if the door opens
        if random.randint(1,10)==1:
            c1=3*10**-5
        else:
            c1=5*10**-7
        if freezertemp[i]>t_point:#logic to se if the tempereture is over 5, if it is, then it cools down.
            c2=8*10**-6
            powerlist[i]=True
        else:
            c2=0
        
        freezertemp[i+1]=freezertemp[i]+(c1*(roomtemp-(freezertemp[i]))+c2*(komptemp-(freezertemp[i])))*deltat
    
    freezertemp.pop()
    #analyze.graphFreezerTemp(freezertemp) #makes a graph of the temperature
    cumcost=analyze.calc_cum_cost(freezertemp,pricelist,powerlist)
    #print(cumcost) DEBUG
    return cumcost
"""
    
def calcTemp(lastTemp,c1,c2,tempKomp,tempRoom,deltaT):
    newTemp=lastTemp+(c1*(tempRoom-(lastTemp))+c2*(tempKomp-(lastTemp)))*deltaT
    return newTemp

def simulateAverage(funktion,cylces,changePoint):
    cumsum=0
    for i in range(cylces):
        cumsum+=funktion(changePoint)
    avg=cumsum/cylces
    return avg

def pricePerTemp(cycles,startPoint,endPoint,step):
    points=np.arange(startPoint,endPoint,step)
    costlist=[0]*len(points)
    i=0
    for temp in points:
        costlist[i]=simulateAverage(simulatesimplelist,cycles,temp)
        i+=1
        print(f"procent af cycle: {(i/len(points))*100}")
    analyze.graphFreezerTemp(costlist,endPoint,start=startPoint,step=step)

def generateRandomBoolArray():
    powerlist=np.zeros(len(get_price_list()))
    for i in range(len(powerlist)):
        if np.random.randint(1,3)==2:
            powerlist[i]=True
        else: powerlist[i]=False
    return powerlist

def simulateAI(AIs,times):
    lowestlist=0
    lowestCost=99999999
    for i in range(AIs):
        powerlist=generateRandomBoolArray()
        cost_list=simKompressor(powerlist,times)
        if cost_list[0]<lowestCost:
            lowestCost=cost_list[0]
            lowestList=cost_list[1]
    print(lowestList)
    return lowestCost

def simKompressor(powerlist,cycles):
    for i in range(cycles):
        pricelist=get_price_list()
        freezertemp=np.array([0.0]*(len(pricelist)+1))
        freezertemp[0]=5.0
        roomtemp=20.0
        komptemp=-5
        deltat=300
        c1=3*10**-5
        c2=8*10**-6
        for i in range(len(freezertemp)-1):#logic for if the door opens
            if random.randint(1,10)==1:
                c1=3*10**-5
            else:                             #make new funktion that checks the food cost/price.
                c1=5*10**-7
            if pricelist[i]==1:
                c2=8*10**-6
            else: c2=0
        freezertemp[i+1]=calcTemp(freezertemp[i],c1,c2,komptemp,roomtemp,deltat)
        
        #freezertemp.pop()
        #analyze.graphFreezerTemp(freezertemp) #makes a graph of the temperature
        cumcost=analyze.calc_cum_cost(freezertemp,pricelist,powerlist)# Returns the cost for the month
    return cumcost, powerlist

def genAI():
    """
    Jeg skal begynde at bruge threading.
    Der skal gemmes den bedste list ud fra hver stage ud fra den mindste cost.
    """
    winnercount=10
    threads=10 #winnercount is equal to threads. because each winner has their own thread.
    randomnes=1 #procent of the list
    samples=100 #amount of simulations of the AI.
    learningCycle=10 #number of times the AI grows.
    aviations=50 #forskellige versioner af den originale liste.



    return True

'''
class farm:
    """
    Represent the data of a farm

    attributes: cows, fodder
    """
    def __init__(self, cows, fodder):
        self.cows = cows
        self.fodder = fodder
        self.average_fodder = self.avg_fodder()

    def avg_fodder(self):
        ans = sum(self.fodder)/(365*self.cows)
        return ans

    def __str__(self):
        return f"The farm has {self.cows} cows."

    def __add__(self, other):
        combined_cows = self.cows + other.cows
        return(farm(combined_cows))

    def __call__(self, days):
        ans = self.cows * self.average_fodder * days
        return ans

min_farm = farm(cows, fodder)
fodder_forbrug = min_farm(10)
print(f"Fodder der skal indkøbes til 10 dages forbrug: {fodder_forbrug:.2f} [ton].")

import pricelist
print("what")
price_list=pricelist.get_price_list()
print(price_list)
print(len(price_list))
class fgf:
    def __init__(self) -> None:
        self.fisk = 1
        return
    
    def yes(self):
        print(self.fisk)

asghd = fgf()
asghd.yes()
print(asghd.fisk)
asghd.efss=3
print(asghd.efss)
'''