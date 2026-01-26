data=[87,"hai","python",8.3,"congratulations"]
new_lst=[]
vowel = 'aeiou'
resultDict = {}

for i in data:
    if type(i)==str:
        new_lst.append(i)

# print(new_lst)

for word in new_lst:
    count=0
    for ch in word.lower():
        if ch in vowel:
            count +=1
    
    resultDict[word.lower()] = count

print(resultDict)


# RECURSION WAY#############
# def word_vowel(lst,out={},i=0):
    # if i<len(lst):
    #     if type(lst[i])==str:
    #         count=0
    #         for ch in 


###333333333333333333
# def count_vowels(data):
#     vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#     for item in data:
#         if isinstance(item, str):
#             for ch in item.lower():
#                 if ch in vowels:
#                     vowels[ch] += 1

#     return vowels


# data = [87, "hai", "python", 8.3, "congratulations"]

# result = count_vowels(data)
# print(result)


# ###########################################################################

# def count_vowels(data):
#     vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#     for item in data:
#         if isinstance(item, str):
#             for ch in item.lower():
#                 if ch in vowels:
#                     vowels[ch] += 1
#     return vowels


# # user input
# data = []
# n = int(input("Enter number of elements: "))

# for i in range(n):
#     val = input("Enter value: ")
#     data.append(val)

# result = count_vowels(data)
# print("Vowel count:", result)













# wapt longest word in the string
# greet='happy makar sankranti whishing you joy prosperity health and success'
# words=greet.split()
# words.sort(key=len)
# print(words[-1])

# st="my name is kajal"
# print({chr:st.count(chr) for chr in st})







# 2.
def rev_str_element(lst,out=set(),i=0):
    if i<len(lst):
        if type(lst[i])==str:
            rev=''
            for ch in lst[i]:
                rev=ch+rev
                out.add(rev)
        else:
            out.add(lst[i])
            rev_str_element(lst,out,i=i+1)
    return out
print(rev_str_element([12,'hai',"hello",87,6.7,'python']))