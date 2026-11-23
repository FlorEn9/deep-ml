import torch
import torch.nn.functional as F

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    """
    Simulates a single neuron with sigmoid activation for binary classification.
    
    Args:
        features: List of feature vectors (each a list of floats)
        labels: List of true binary labels
        weights: Neuron weights (one per feature)
        bias: Neuron bias term
    
    Returns:
        Tuple of (predicted probabilities rounded to 4 decimal places, MSE rounded to 4 decimal places)
    """
    # Your code here using PyTorch built-ins:
    # - torch.matmul() for linear combination
    # - torch.sigmoid() for activation
    # - torch.nn.functional.mse_loss() for MSE
    features=torch.tensor(features,dtype=torch.float64)
    z=0
    zl=[]
    for i in range(features.shape[0]):
        for j in range(features.shape[1]):
            z+=features[i][j]*weights[j]
        zl.append(z+bias)
        z=0
    zl=torch.stack(zl)
    zl=torch.sigmoid(zl)
    
    labels=torch.tensor(labels,dtype=torch.float64)
    mse=torch.nn.functional.mse_loss(zl,labels)
    zl=zl.tolist()
    mse=mse.item()
    a=(zl,mse)
    return a
    pass