import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplt as plt

def fode(i,t,cpi):
    solI = i*cpi
    return solI

#initial condition
io = 0.1

#create array of time points
timePoints = np.linspace(0, 10, 11)
print(timePoints)

#solve ODE
cpi = 0.3
solution = odeint(fode,io,timePoints,args=(cpi,))
print(solution)

#set data points on plot
plt.plot(timePoints,solution)

#label x- and y- axes
plt.xlabel('time')
Text(0.5, 0, 'time')
plt.ylabel('i(t)')
Text(0, 0.5, 'i(t)')

#set the position of text and display desired text
yMax = max(solution)
xMax = max(timePoints)

plt.text(0.8*xMax,0.8*yMax,str("cpi="+str(cpi)))
plt.text(0.8*xMax,0.7*yMax,str("i(o)="+str(io)))

>>> #display the plot
>>> plt.show()
