# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:18:06 2019

@author: Gunzshooter
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:00:57 2019

@author: Hans Pot

Creates tafel plots using the filename as legend input
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
import glob


pd.set_option('display.max_rows', None)
tafel = pd.read_csv('$10^0$ mBar.txt',delimiter=';')

potentialApplied = tafel["Potential applied (V)"]
current = tafel["WE(1).Current (A)"]

    
#The minimum current index e.i. reverse of reaction

index = abs(current).idxmin()
    
anodic_current = current[index:]
anodic_potential = potentialApplied[index:]


p = np.polyfit(abs(anodic_current), np.log(abs(anodic_potential)), 1)



plt.plot(abs(anodic_current),anodic_potential,'--',mew = '2', label = '1 mBar') 

plt.title("Matplotlib demo") 
plt.xlabel("Current Density (A/cm$^2$)")
plt.ylabel("Potential Applied (V)") 
    
csvFiles = glob.glob("*.txt")
      
    
#plt.ylim(-2, 0)
#plt.xlim(0.00000001,1)


plt.xscale("log")
plt.legend()
plt.savefig('plot.png',dpi=600) 




#%%
"""
Corrosion Potential
"""

corrosion_Potential = round(potentialApplied[abs(current).idxmin()],2)
print('Corrosion Potential: ' + str(corrosion_Potential))


