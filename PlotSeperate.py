
"""
Created on Mon Sep 30 21:00:57 2019

@author: Hans Pot

Creates tafel plots using the filename as legend input
"""

import pandas as pd
from matplotlib import pyplot as plt 
import glob

def plotTafel(fileName):
    pd.set_option('display.max_rows', None)
    tafel = pd.read_csv(fileName,delimiter=';')
    #Remove Current overloads from plot
    try:
        tafel = tafel[tafel.Overload != 'Current overload']
    except:
        print('no overloads')

    potentialApplied = tafel["Potential applied (V)"]
    current = tafel["WE(1).Current (A)"]

    #Duplicate this line to show multiple plots in one figure
    plt.plot(abs(current),potentialApplied,'--',mew = '2', label = fileName.replace('.txt','')) 

    #plt.title("Substrate") 
    plt.xlabel("Current Density (A/cm$^2$)")
    plt.ylabel("Potential Applied (V)") 
    
    
    """
    Corrosion Potential
    """
    corrosion_Potential = round(potentialApplied[abs(current).idxmin()],2)
    print(fileName)
    print('Corrosion Potential: ' + str(corrosion_Potential))
    
    #plt.ylim(-2, 0)
    #plt.xlim(0.00000001,1)


    plt.xscale("log")
    #plt.show()

    plt.savefig(fileName.replace('.txt','') + '.png',dpi=600)   
    
    
csvFiles = glob.glob("*.txt")
      
for file in csvFiles:
    plotTafel(file)
    #Clears Figure
    plt.clf()

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    