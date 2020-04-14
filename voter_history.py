import numpy as np      #imports libraries
import matplotlib.pyplot as plt
from scipy.stats import linregress
"""
Predicts voter percentage for the next election.

In every array defined in this code, the first column corresponds to data for the
Parti Libéral, second corresponds to Parti Québécois, third corresponds to 
Coalition Avenir Québec, fourth to Québec Solidaire and fifth to Other.
"""
data=np.loadtxt("data.csv",delimiter=",")            #load data from file
year=np.array([1998,2003,2007,2008,2012,2014,2018])  #define arrays needed for analysis
yearpresent=np.append(year,2022)

def average(data):         #find the average vote for each party
    avg=np.array([0.,0.,0.,0.,0.])

    for i in range(5):
        avg[i]=np.average(data[:,i])

    for i in range(5):     #normalizes data to 100%.
        avg[i]=avg[i]/np.sum(avg)*100
        
    return avg

def linreg(year, data):    #finds the linear regression for each party's voting history
    lreg=linregress(year, data[:,0]) #computes linear regression l is short for libéral
    preg=linregress(year, data[:,1]) #p is short for parti québécois
    creg=linregress(year, data[:,2]) #c is short for coalition
    qreg=linregress(year[2:], data[2:,3]) #q is short for québec solidaire
    oreg=linregress(year, data[:,4]) #o is short for other

    slopes=([lreg[0],preg[0],creg[0],qreg[0],oreg[0]])
    intercepts=([lreg[1],preg[1],creg[1],qreg[1],oreg[1]])
    
    linpercent=np.array([2022*slopes[0]+intercepts[0],2022*slopes[1]+intercepts[1],+2022*slopes[2]+intercepts[2],2022*slopes[3]+intercepts[3],2022*slopes[4]+intercepts[4]])
    linpercent=linpercent/sum(linpercent)*100   #normalizes data to 100%
    
    return linpercent

def weightreg(year, data):  #finds the weighted linear regression for each party
    weight=np.array([1/25,6/25,10/25,11/25,15/25,17/25,21/25])  #defines weights
    
    lreg=linregress(year, data[:,0]*weight)    
    preg=linregress(year, data[:,1]*weight)
    creg=linregress(year, data[:,2]*weight)
    qreg=linregress(year[2:], data[2:,3]*weight[2:])
    oreg=linregress(year, data[:,4]*weight)

    wpercent=np.array([2022*lreg[0]+lreg[1],2022*preg[0]+preg[1],+2022*creg[0]+creg[1],2022*qreg[0]+qreg[1],2022*oreg[0]+oreg[1]])
    wpercent=wpercent/sum(wpercent)*100  #normalizes
    
    return wpercent

avg=average(data)    #uses the functions to get percentages
linpercent=linreg(year,data)
wpercent=weightreg(year,data)

plt.plot(year,data[:,0], "r.-",label="Parti Libéral")   #plots results
plt.plot(2022,wpercent[0], marker="^", linestyle=" ", color='r')
plt.plot(2022,linpercent[0], marker="s", linestyle=" ", color='r')
plt.plot(2022,avg[0], marker="d", linestyle=" ", color='r')

plt.plot(year,data[:,1], "b.-",label="Parti Québécois")
plt.plot(2022,wpercent[1], marker="^", linestyle=" ", color='b')
plt.plot(2022,linpercent[1], marker="s", linestyle=" ", color='b')
plt.plot(2022,avg[1], marker="d", linestyle=" ", color='b')

plt.plot(year,data[:,2], "c.-",label="Coalition Avenir Québec")
plt.plot(2022,wpercent[2], marker="^", linestyle=" ", color='c')
plt.plot(2022,linpercent[2], marker="s", linestyle=" ", color='c')
plt.plot(2022,avg[2], marker="d", linestyle=" ", color='c')

plt.plot(year[2:],data[2:,3], marker=".", linestyle="-", color="tab:orange", label="Québec Solidaire")
plt.plot(2022,wpercent[3], marker="^", linestyle=" ", color='tab:orange')
plt.plot(2022,linpercent[3], marker="s", linestyle=" ", color='tab:orange')
plt.plot(2022,avg[3], marker="d", linestyle=" ", color='tab:orange')

plt.plot(year,data[:,4], "k.-", label="Other")
plt.plot(2022,wpercent[4], marker="^", linestyle=" ", color='k',label="Weighted Linear Regression")
plt.plot(2022,wpercent[4], marker="s", linestyle=" ", color='k',label="Linear Regression")
plt.plot(2022,avg[4], marker="d", linestyle=" ", color='k', label="Average")

plt.xticks(yearpresent)
plt.xlabel("Year")
plt.ylabel("Percentage of vote")
plt.title("Prediction of the Percentage of Votes")
plt.legend(loc="lower left")

print(average(data))  #prints percentages
print(linreg(year,data))
print(weightreg(year, data))