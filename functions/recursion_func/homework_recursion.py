data=[87,"hai","python",8.3,"congratulations"]
new_lst=[]
vowel = 'aeiou'
resultDict = {}

for i in data:
    if type(i)==str:
        new_lst.append(i)

print(new_lst)

for word in new_lst:
    count=0
    for ch in word.lower():
        if ch in vowel:
            count +=1
    
    resultDict[word.lower()] = count

print(resultDict)












# wapt longest word in the string
# greet='happy makar sankranti whishing you joy prosperity health and success'
# words=greet.split()
# words.sort(key=len)
# print(words[-1])

# st="my name is kajal"
# print({chr:st.count(chr) for chr in st})