data=[87,"hai","python",8.3,"congratulations"]
new_lst=[]
for i in data:
    if type(i)==str:
        new_lst.append(i)
        print("yes it string")
    else:
        print("no a string")
# wapt longest word in the string
greet='happy makar sankranti whishing you joy prosperity health and success'
words=greet.split()
words.sort(key=len)
print(words[-1])