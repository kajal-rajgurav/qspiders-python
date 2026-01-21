# building a dict of word and length pair.
sentence='this is a bunch of words'
word_len={}
for i in sentence.split():
    word_len[i]=len(i)
print(word_len)

# ...comprehension way.........
print({i:len(i) for i in sentence.split()})