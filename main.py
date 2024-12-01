"""
Main, where it all begins.
"""
import freezer
import analyze

print("enter ('1') to simulate the cost of 1 month with simple thermostat")
print("enter ('2') to simulate the average cost of different changepoints, where this returns a graph")
print("enter ('3') to simulate average cost of a specific changepoint over a given amount cycles")
input1=input()
if input1=='1':
    input1=float(input("enter 'changepoint' example: '6.25' Enter:"))
    print(f"cost of one month with {input1}C as changepoint: {freezer.simulatesimplelist(input1)}kr.-")
    
elif input1=='2':
    input1=(input("input 'cycles, startpoint, endpoint, step' example: '10,6.2,6.4,0.01' Enter:")).split(',')
    costlist=freezer.pricePerTemp(int(input1[0]),float(input1[1]),float(input1[2]),float(input1[3]))
    analyze.graphlist(costlist,float(input1[2]),'Skifte-Temperatur [C]','Udgifter [kr.]',start=float(input1[1]),step=float(input1[3]))

elif input1=='3':
    input1=input("input 'cycles, changePoint' example: '100,6.25' Enter:").split(',')
    print(f"cost of an average month with {input1[1]}C as changepoint with {input1[0]} cycles: {freezer.simulateAverage(freezer.simulatesimplelist,int(input1[0]),float(input1[1]))}kr.-")
