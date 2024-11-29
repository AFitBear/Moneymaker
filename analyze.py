import matplotlib.pyplot as plt
import numpy as np

def gg():
    print("gggff")
    return True


def graphFreezerTemp(theList, start=1,step=1):#plot list nameIdea:"plotList"
    #if start==1 and step==1:
    #    x =x = np.arange(start,len(theList)+1,step)
    x = np.arange(start,6.3+0*(start+len(theList)),step)
    #plt.plot(x, len(theList])
    plt.plot(x,theList)
    plt.xlabel('Skifte-Temperatur [C]') #5min intervalantal
    plt.ylabel('Udgifter [kr.]') #Temperatur [C]
    plt.grid()
    plt.show()
    plt.savefig('graphOfFreezer.PNG')
    return True

def calc_cum_cost(freezertemp,pricelist,powerlist):
    freezertemp=np.delete(freezertemp,-1)
    cumcost=0
    cumfoodcost=0
    cumcostlist=np.array([0]*len(freezertemp))
    for i in range(len(freezertemp)):#calcultes powercost, if the compressor was on it cost 1whr which is just 1 times the price
        if powerlist[i]:
            cumcost+=pricelist[i]
        cumcost+=calculateFoodCost(freezertemp[i])#calculates foodcost

    #graphFreezerTemp(cumcostlist)
    #print(f'Madkost er {cumfoodcost}') DEBUG
    return cumcost

def calculateFoodCost(temp):
    """
    Calculates the food cost according to the temperature given
    """
    if temp<3.5:#calculates foodcost
        foodCost=4.39*np.exp(-0.49*temp)
    elif temp>6.5:#calculates foodcost
        foodCost=0.11*np.exp(0.31*temp)
    else: return 0
    return foodCost