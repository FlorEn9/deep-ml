import numpy as np
import math

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    

    # Your code here
    B=A.T@A
    if(B[0,0]==B[1,1]):
        sigma=math.pi/4
    else:sigma=(1/2)*np.arctan(2*B[0,1]/(B[0,0]-B[1,1]))
    R=[[math.cos(sigma),-math.sin(sigma)],[math.sin(sigma),math.cos(sigma)]]
    R=np.array(R)
    D=R.T@(A.T@A)@R
    S=[math.sqrt(D[0,0]),math.sqrt(D[1,1])]
    S=np.array(S)
    idx=np.argsort(S)
    idx=idx[::-1]
    S=S[idx]
    R=R[:,idx]
    E=np.diag(1/np.array(S))
    U=A@R@E
    return (U,S,R.T)
    pass