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
    plt.xlabel('Udgifter [kr.]') #5min intervalantal
    plt.ylabel('Skifte-Temperatur [C]') #Temperatur [C]
    plt.grid()
    plt.show()
    #plt.savefig()
    return True

def calc_cum_cost(freezertemp,pricelist,powerlist):
    cumcost=0
    cumfoodcost=0
    cumcostlist=[0]*len(freezertemp)
    for i in range(len(freezertemp)):#calcultes powercost, if the compressor was on it cost 1whr which is just 1 times the price
        if powerlist[i]:
            cumcost+=pricelist[i]
        if freezertemp[i]<3.5:#calculates foodcost
            cumcost+=4.39*np.e**(-0.49*freezertemp[i])
            cumfoodcost+=4.39*np.e**(-0.49*freezertemp[i])
        elif freezertemp[i]>6.5:#calculates foodcost
            cumcost+=0.11*np.e**(0.31*freezertemp[i])
            cumfoodcost+=0.11*np.e**(0.31*freezertemp[i])
        cumcostlist[i]=cumcost

    #graphFreezerTemp(cumcostlist)
    print(f'Madkost er {cumfoodcost}')
    return cumcost