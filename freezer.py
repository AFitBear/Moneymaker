import random
import data
from pricelist import get_price_list
import numpy
#import analyze

def simulate():
    pricelist=get_price_list()
    datalist=[data]*len(pricelist)
    datalist[0].temp=2
    print(len(pricelist))

    roomtemp=20
    komptemp=-5
    deltat=300
    dooropen=False
    power=1
    freezertemp=0
    tnew=0

    #datalist[]
    for times in datalist:
        if (random.randint(1,11)==1):
            dooropen=True
        else: 
            dooropen=False
    
    Tnew=datalist[0]






    return datalist




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