import math
from collections import Counter

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    sum=0
    c=Counter(labels)
    
    for i in c.values():
        sum+=(i/len(labels))*math.log(i/len(labels),2)
    sum=sum*(-1)
    return sum
    
    pass

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    # Your code here
    labels=[]
    for example in examples:
        labels.append(example[target_attr])
    ent=calculate_entropy(labels)
    values=set()
    for example in examples:
        values.add(example[attr])
    s=0
    for value in values:
        sublist=[]
        for example in examples:
            if value==example[attr]:
                sublist.append(example[target_attr])
        entd=calculate_entropy(sublist)
        wv=len(sublist)/len(examples)
        s+=wv*entd
    return ent-s


    
    pass

def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    # Your code here
    l=[]
    for example in examples:
        l.append(example[target_attr])
    c=Counter(l)
    

    x=Counter.most_common(c)
    f=x[0][1]
    s=[]
    for i in x:
        if i[1]==f:
            s.append(i)
    p=sorted(s)


    return p[0][0]
    pass

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    """Build a decision tree using the ID3 algorithm."""
    # Your code here
    x=majority_class(examples,target_attr)
    values=set()
    for example in examples:
        values.add(example[target_attr])
    if len(values)==1:
        return values.pop()
    if len(attributes)==0:
        return x
    m=-1
    p=0
    for atribut in attributes:
        k=calculate_information_gain(examples,atribut,target_attr)
        if k>m:
            m=k
            p=atribut
    setp=set()
    for example in examples:
        setp.add(example[p])
    new={}
    fara=[]
    for atribut in attributes:
        if atribut!=p:
            fara.append(atribut)

    for value in sorted(setp):
        sublist=[]
        for example in examples:
            if value==example[p]:
                sublist.append(example)
        new[value]=(learn_decision_tree(sublist,fara,target_attr))
    return {p:new}
        
    



    pass