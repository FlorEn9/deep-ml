import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    
    if arr.ndim==1 and norm_type=='frobenius':
        raise ValueError("Tre sa fie 2D")
    else:
        x=arr.flatten()
        
        if norm_type=='l1':
            s=0
            for j in range(len(x)):
                s+=(abs(x[j]))
            return s
        if norm_type=='l2':
            s=0
            for i in range(len(x)):
                s+=x[i]**2
            return np.sqrt(s)
        if norm_type=='linf':
            return(max(abs(x)))
        if norm_type=='frobenius':
            s=0
            for i in range(len(x)):
                s+=x[i]**2
            return np.sqrt(s)



            
        
        
        
    pass
