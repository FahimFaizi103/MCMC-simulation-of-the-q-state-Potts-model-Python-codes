
import numpy as np
from Func_Boltzmann_weights_Potts import Boltzmann_weights_Potts
import time

#%%
J = 1
kT = 0.910
numSpinsPerDim = 4
numSweeps = 10**4
equilib_time = round(0.1*numSweeps)
#%%
min_q = 1
max_q = 4
#%%
Mmean = np.zeros(numSweeps)
spin = np.random.randint(min_q, max_q +1, size=(numSpinsPerDim, numSpinsPerDim))
q_states = list(range(min_q, max_q+1)) # possible spin states.

#%%

# Sample spins randomly. 
t = time.time()
for SweepIndex in range(0,numSweeps,1):
    for i in range(0,np.size(spin),1):
        
        
        row = np.random.randint(0,np.size(spin,0)) # produces a random integer between [0,size of rows). i.e. (1,101) produces number between 1 and 100.  
        col = np.random.randint(0,np.size(spin,1)) 
        
        above = ( (row -1 )%(np.size(spin,0)) ) 
        below = ( (row +1 )%(np.size(spin,0)) ) 
        left  = ( (col -1 )%(np.size(spin,1)) ) 
        right = ( (col +1 )%(np.size(spin,1)) ) 
        
        neighbors = [spin[above,col], spin[row,left], spin[row,right], spin[below,col]]
        
        [Boltzmann_weights] = Boltzmann_weights_Potts(q_states, neighbors, J, kT)
        
        P = Boltzmann_weights/np.sum(Boltzmann_weights)
        
        new_state = np.random.choice(q_states, p = P)
        
        spin[row,col] = new_state
       
    
    Mmean[SweepIndex] = np.mean(spin)

elapsed = time.time() - t
print("Time elapsed:", elapsed)

