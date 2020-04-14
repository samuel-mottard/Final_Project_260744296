import numpy as np #imports libraries
import matplotlib.pyplot as plt
"""
Monte Carlo simulation to determine the winner of next Québec elections
based on percentages found in voter_history.py
"""
data=np.loadtxt("2018_results.csv",delimiter=",") #loads datato find standard deviation

n=125 #number of constituencies

#define the weight given to each percentages
pollweight=0.5   #poll percentage weight
linweight=0.0    #linear regression percentage weight
weiregweight=0.5 #weighted linear regression percentage weight
aveweight=0.0    #average percentage weight

#calculates weighted 
lpercent=pollweight*19.2+linweight*25.9+weiregweight*29.85+aveweight*37.52         #+24.82   #part in comments
ppercent=pollweight*14.4+linweight*15.62+weiregweight*21.52+aveweight*30.40        #+17.06   #is results of
cpercent=pollweight*51.9+linweight*36.29+weiregweight*29.89+aveweight*23.41        #+37.42   #2018 election
qpercent=pollweight*10.4+linweight*17.74+weiregweight*14.92+aveweight*5.43         #+16.1
opercent=pollweight*4+linweight*4.44+weiregweight*3.82+aveweight*3.28              #+4.6

ldev=np.std(data[:,0]) #computes standard deviations for each party
pdev=np.std(data[:,1])
cdev=np.std(data[:,2])
qdev=np.std(data[:,3])
odev=np.std(data[:,4])

run=1000  #number of runs the simulation does


winner=np.array([0,0,0,0,0,0]) #arrays needed for simulation
num_const=np.array([0,0,0,0,0])

for i in range(run):
    l=np.random.normal(lpercent, ldev, n)  #generates 125 random numbers, gaussian distributed
    p=np.random.normal(ppercent, pdev, n)  #around percentage calculated above
    c=np.random.normal(cpercent, cdev, n)  #standard dev found above
    q=np.random.normal(qpercent, qdev, n)
    o=np.random.normal(opercent, odev, n)
    lwin=0
    pwin=0
    cwin=0
    qwin=0
    owin=0    
    for j in range(n):   #determines winner of each of the 125 constitencies
        const_percent=l[j]+p[j]+c[j]+q[j]+o[j]
        l[j]=l[j]/const_percent #normalizes percentages to 100
        p[j]=p[j]/const_percent
        c[j]=c[j]/const_percent
        q[j]=q[j]/const_percent
        o[j]=o[j]/const_percent
        if l[j]>p[j] and l[j]>c[j] and l[j]>q[j] and l[j]>o[j]: #if statement to find max
            lwin=lwin+1
        elif p[j]>l[j] and p[j]>c[j] and p[j]>q[j] and p[j]>o[j]:
            pwin=pwin+1
        elif c[j]>l[j] and c[j]>p[j] and c[j]>q[j] and c[j]>o[j]:
            cwin=cwin+1        
        elif q[j]>l[j] and q[j]>p[j] and q[j]>c[j] and q[j]>o[j]:
            qwin=qwin+1
        elif o[j]>l[j] and o[j]>p[j] and o[j]>c[j] and o[j]>q[j]:
            owin=owin+1
    
    if lwin>pwin and lwin>cwin and lwin>qwin and lwin>owin: #if statements to find who has most seats
        winner[0]=winner[0]+1
    elif pwin>lwin and pwin>cwin and pwin>qwin and pwin>owin:
        winner[1]=winner[1]+1
    elif cwin>lwin and cwin>pwin and cwin>qwin and cwin>owin:
        winner[2]=winner[2]+1
    elif qwin>lwin and qwin>pwin and qwin>cwin and qwin>owin:
        winner[3]=winner[3]+1
    elif owin>lwin and owin>pwin and owin>cwin and owin>qwin:
        winner[4]=winner[4]+1
    else:
        winner[5]=winner[5]+1
    
    num_const[0]=num_const[0]+lwin #finds total number of constituencies
    num_const[1]=num_const[1]+pwin #won for the whole simulation
    num_const[2]=num_const[2]+cwin #for each party
    num_const[3]=num_const[3]+qwin
    num_const[4]=num_const[4]+owin
    

num_const=num_const/run #finds the average number of constituencies won


labels1= "Parti Libéral", "Parti Québécois", "Coalition Avenir Québec", "Québec Solidaire", "Others", "Tie"
labels2= "Parti Libéral", "Parti Québécois", "Coalition Avenir Québec", "Québec Solidaire", "Others"
colors1= "r", "b", "c", "tab:orange", "k", "g"
colors2= "r", "b", "c", "tab:orange", "k"

plt.subplot(1,2,1) #displays results
plt.pie(winner, labels=labels1, colors=colors1,autopct='%1.1f%%')
plt.title("Probability of Winning the Next Election")
#plt.title("Simulation of 2018 Election's Winner Based on Vote-shares")

plt.subplot(1,2,2)
plt.pie(num_const, labels=labels2, colors=colors2,autopct=lambda num_const: "{:.1f}".format(num_const*1.25))
plt.title("Predicted Number of Won Constituencies")
#plt.title("Simulated Number of Constituencies Won by Each Party in 2018")