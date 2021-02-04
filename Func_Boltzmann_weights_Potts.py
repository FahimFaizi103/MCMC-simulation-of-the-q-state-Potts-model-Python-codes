#% Computing Bolztmann weights

def Boltzmann_weights_Potts(q_states, neighbors, J, kT):
    
    import numpy as np
    
    #%% initialize vectors
    Boltzmann_weights = np.zeros(np.size(q_states))
     
    #%% Compute Bolztmann weights
    for i in range (0,np.size(q_states),1):
        
        state = q_states[i]
        
        interaction_after_flip = neighbors[:]
        
        interaction_after_flip[:] = [x if x == state else 0 for x in interaction_after_flip]
        interaction_after_flip[:] = [x if x != state else 1 for x in interaction_after_flip]
        
        E_bath = -J*(np.sum(interaction_after_flip))
        
        Boltzmann_weights[i] = np.exp(-E_bath/kT)
        
    return[Boltzmann_weights]
        
        
        