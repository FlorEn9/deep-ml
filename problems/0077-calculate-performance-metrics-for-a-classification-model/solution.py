import numpy as np
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    # Implement your code here
    l=[]
    
    actual=np.array(actual)
    predicted=np.array(predicted)
    TP=0
    TN=0
    FN=0
    FP=0
    for i in range(len(actual)):
        if actual[i]==predicted[i]:
            if actual[i]==1:
                TP+=1
            else:TN+=1
        
        elif actual[i]==1:
            FN+=1
        else:FP+=1
    x=[]
    x.append(TP)
    x.append(FN)
    l.append(x)
    x=[]
    x.append(FP)
    x.append(TN)
    l.append(x)
    l=np.array(l)
    
    
    accuracy=(l[0,0]+l[1,1])/(np.sum(l))
    precision=(l[0,0])/(l[0,0]+l[1,0])
    negativePredictive=(l[1,1])/(l[1,1]+l[0,1])
    recall=(l[0,0])/(l[0,0]+l[0,1])
    specificity=(l[1,1])/(l[1,1]+l[1,0])
    f1=2*(precision*recall)/(precision+recall)
    confusion_matrix=l
    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
