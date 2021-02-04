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
Mmean = np.zeros(int(numSweeps))
spin = np.random.randint(min_q, max_q +1, size=(numSpinsPerDim, numSpinsPerDim))

#%%
t = time.time()
for Sweepindex in range(0,int(numSweeps),1):
    
    for row in range(0,numSpinsPerDim,1):
        
        for col in range(0,numSpinsPerDim,1):
            
            q_states = list(range(min_q, max_q+1)) # possible spin states.
            
            above = ( (row -1 )%(np.size(spin,0)) ) 
            below = ( (row +1 )%(np.size(spin,0)) ) 
            left  = ( (col -1 )%(np.size(spin,1)) ) 
            right = ( (col +1 )%(np.size(spin,1)) ) 
            
            neighbors = [spin[above,col], spin[row,left], spin[row,right], spin[below,col]]
            
            [Boltzmann_weights] = Boltzmann_weights_Potts(q_states, neighbors, J, kT)
            
            max_weight = np.max(Boltzmann_weights) # Figure out the maximum weight
            max_weight_position = np.where(Boltzmann_weights == max_weight) # figure out the index of the maximum weight
            max_weight_position = max_weight_position[0][0] # if there are two or more maximum weights, choose one.
            
            Boltzmann_weights[0], Boltzmann_weights[max_weight_position] = Boltzmann_weights[max_weight_position], Boltzmann_weights[0] # rearrange the maximum weight at the front of the vector
            q_states[0], q_states[max_weight_position] = q_states[max_weight_position], q_states[0]
            
            index = q_states.index(spin[row,col])
            Current_weight = Boltzmann_weights[index]
            
            S_i = np.sum(Boltzmann_weights[0:index+1])
            
            P = np.zeros(np.size(q_states))
            v = np.zeros(np.size(q_states))
           
            for j in range(0,np.size(q_states),1):
                
                Final_weight = Boltzmann_weights[j]
                
                if j == 0:
                    S_j_1 = np.sum(Boltzmann_weights)
                else:
                    S_j_1 = np.sum(Boltzmann_weights[0:j])
                    
                Delta = S_i - S_j_1 + max_weight
                
                arg = np.array([Delta, (Current_weight + Final_weight - Delta), Current_weight, Final_weight])
                v[j] = max(0,np.min(arg))
                
                P[j] = v[j]/Current_weight
            
            new_state = np.random.choice(q_states, p = P)
            spin[row,col] = new_state
        
    Mmean[Sweepindex] = np.mean(spin)
    
elapsed = time.time() - t
print("Time elapsed:", elapsed) 
   
    
#np.savetxt("ST.dat", Mmean)
#np.savetxt("spin.dat",spin)
 