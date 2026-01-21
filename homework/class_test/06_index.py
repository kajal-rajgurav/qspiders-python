2.flipping keys and values of the dictionary using dict comrehension
# 
d={'a':1,'b':2,'c':3,'d':1} 
flipped={k:v for v,k in d.items()}
print(flipped)

# another way



# 3.counting the numbers of each character in a string 
sentence='hello world welcomes to hello world python   '
print({ch:sentence.count(ch) for ch in  sentence})


# 4.create a dict of word and its count pair from given string 
sentence='hello world welcomes to hello world python   '
