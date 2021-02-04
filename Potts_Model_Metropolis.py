import numpy as np
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

#%% initializing vectors
Mmean = np.zeros(numSweeps)

#%% Sample spins randomly. 

spin = np.random.randint(min_q, max_q +1, size=(numSpinsPerDim, numSpinsPerDim,))

t = time.time()

for SweepIndex in range(0,numSweeps,1):
       
    
    for i in range(0,np.size(spin),1):
        
        q_states = list(range(min_q, max_q+1)) # possible  spin states.
        
        row = np.random.randint(0,np.size(spin,0)) # prduces a random integer between [0,size of rows). i.e. (1,101) produces number between 1 and 100.  
        col = np.random.randint(0,np.size(spin,1)) 
        
        above = ( (row -1 )%(np.size(spin,0)) ) 
        below = ( (row +1 )%(np.size(spin,0)) ) 
        left  = ( (col -1 )%(np.size(spin,1)) ) 
        right = ( (col +1 )%(np.size(spin,1)) ) 
        
        neighbors = [spin[above,col], spin[row,left], spin[row,right], spin[below,col]]
        
        interaction_before_flip = neighbors[:]
        interaction_before_flip[:] = [x if x == spin[row,col] else 0 for x in interaction_before_flip]
        interaction_before_flip[:] = [x if x != spin[row,col] else 1 for x in interaction_before_flip]
        
        q_states.remove(spin[row,col])
        new_state = np.random.choice(q_states) # randomly select a spin from q_states choices.
        
        interaction_after_flip = neighbors[:]
        interaction_after_flip[:] = [x if x == new_state else 0 for x in interaction_after_flip]
        interaction_after_flip[:] = [x if x != new_state else 1 for x in interaction_after_flip]
        
        
        dE = -J*(np.sum(interaction_after_flip) - np.sum(interaction_before_flip))
        
        P = np.exp(-dE/kT)
        
        u = np.random.uniform(0,1)
        
        if u<= min(1,P):
            spin[row,col] = new_state
        else:
            spin[row,col] =  spin[row,col]
    
    Mmean[SweepIndex] = np.mean(spin)
    
elapsed = time.time() - t
print("Time elapsed:", elapsed)
        



       
        
       
    
      
    
    
    
    

  
    
