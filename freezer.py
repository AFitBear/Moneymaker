import random
import data
import analyze
from pricelist import get_price_list
import numpy as np
#import analyze

stop_at_number=0#8500 #edit here
def simulatesimplelist(changepoint):
    pricelist=get_price_list()
    powerlist=np.array([False]*len(pricelist))
    freezertemp=np.array([0.0]*(len(pricelist)+1-stop_at_number))
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
        
        freezertemp[i+1]=freezertemp[i]+(c1*(roomtemp-(freezertemp[i]))+c2*(komptemp-(freezertemp[i])))*deltat
    
    #freezertemp.pop()
    #analyze.graphFreezerTemp(freezertemp) #makes a graph of the temperature
    cumcost=analyze.calc_cum_cost(freezertemp,pricelist,powerlist)
    print(cumcost)
    return True





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
    print(cumcost)
    return cumcost

def simulateAverage(cylces,t_point):
    cumsum=0
    for i in range(cylces):
        cumsum+=simulateAIlist(t_point)
        print(f"procent af cycle: {(i/cylces)*100}")
    avg=cumsum/cylces
    return avg

def pricePerTemp(cycles):
    points=np.arange(6.1,6.3,0.01)
    costlist=[0]*len(points)
    i=0
    for temp in points:
        costlist[i]=simulateAverage(cycles,temp)
        i+=1
    analyze.graphFreezerTemp(costlist,6.1,0.01)


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