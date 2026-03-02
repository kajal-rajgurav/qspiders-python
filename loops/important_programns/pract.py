# 2.flipping keys and values of the dictionary using dict comrehension
 
d={'a':1,'b':2,'c':3,'d':1} 
flipped={k:v for v,k in d.items()}
print(flipped)