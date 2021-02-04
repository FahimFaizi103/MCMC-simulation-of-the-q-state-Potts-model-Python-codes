#% Computing Bolztmann weights

def Metropolizing(P, loc):
    
    import numpy as np
    
    #%% initialize vectors
    P_MG = np.zeros(np.size(P))
     
    #%% Metropolizing
    P_current = P[loc]
    
    P1 = P/(1 - P_current)
    P2 = P/(1 - P)
    
    for i in range(0, np.size(P),1):
        
        if i == loc:
            continue
        else:
            P_MG[i] = min(P1[i], P2[i])
    
    P_MG[loc] = 1 - np.sum(P_MG)
    
    return[P_MG]
        
        
        
        
