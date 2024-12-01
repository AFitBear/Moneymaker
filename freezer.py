"""
Module where the freezer operates and the logic of the freezer is executed.
"""
import random
import analyze
from pricelist import get_price_list
import numpy as np

class Freezerroom:
    """
    class that have basic data of the freezer
    """
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



if __name__== '__main__':
    import doctest
    print(doctest.testmod)





"""
def pricePerTempTEST(cycles, startPoint, endPoint, step):
    points = np.arange(startPoint, endPoint, step)
    costlist = [0] * len(points)
    threads = []

    # Lock to manage shared resources
    costlist_lock = threading.Lock()

    def worker(index, temp):
       Worker function to compute simulateAverage for a given temperature.
        cost = simulateAverage(simulatesimplelist, cycles, temp)
        with costlist_lock:  # Ensure thread-safe write to the shared list
            costlist[index] = cost
        print(f"Thread {threading.current_thread().name}: Completed simulation for temp {temp}.")

    # Create and start a thread for each temperature
    for i, temp in enumerate(points):
        thread = threading.Thread(target=worker, args=(i, temp), name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Analyze and graph the results
    analyze.graphFreezerTemp(costlist, endPoint, 'Skifte-Temperatur [C]', 'Udgifter [kr.]', start=startPoint, step=step)

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
    
    Jeg skal begynde at bruge threading.
    Der skal gemmes den bedste list ud fra hver stage ud fra den mindste cost.
    
    winnercount=10
    threads=10 #winnercount is equal to threads. because each winner has their own thread.
    randomnes=1 #procent of the list
    samples=100 #amount of simulations of the AI.
    learningCycle=10 #number of times the AI grows.
    aviations=50 #forskellige versioner af den originale liste.
    return True
"""