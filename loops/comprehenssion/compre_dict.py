# building a dict of word and length pair.
sentence='this is a bunch of words'
word_len={}
for i in sentence.split():
    word_len[i]=len(i)
print(word_len)

# ...comprehension way.........
print({i:len(i) for i in sentence.split()})


# 2.flipping keys and values of the dictionary using dict comrehension
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
print({word:sentence.count(word) for word in  sentence.split()})


# 5.dict of character and ascii value pairs

s='abcABC'
print({ ch:ord(ch) for ch in s})

# 6.create a dict of bulidings by converting there height from meter to feet . 

buildings={
    'burj khalifa':828,
    'shanghao tower':632,
    'abc':435
}
print({ building:height*3.28 for building,height in buildings.items()})

# 7.creating dict of city and populATION pairs using dict comprehsion
citis