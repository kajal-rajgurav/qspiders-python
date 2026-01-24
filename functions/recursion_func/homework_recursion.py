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


###333333333333333333
def count_vowels(data):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for item in data:
        if isinstance(item, str):
            for ch in item.lower():
                if ch in vowels:
                    vowels[ch] += 1

    return vowels


data = [87, "hai", "python", 8.3, "congratulations"]

result = count_vowels(data)
print(result)












# wapt longest word in the string
# greet='happy makar sankranti whishing you joy prosperity health and success'
# words=greet.split()
# words.sort(key=len)
# print(words[-1])

# st="my name is kajal"
# print({chr:st.count(chr) for chr in st})