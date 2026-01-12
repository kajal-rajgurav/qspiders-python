# wapt list of  num of range b/w 1 to 20.

# print([i for i in range(1,21)])


# wapt list of character in given string.
# greet='hello world'
# char=[i for i in greet]
# print(char)
     
# wapt list of sqaure numbwrs which are present given list.
# numbers=[1,2,3,4,5]
# sqr=[i**2 for i in numbers]
# print(sqr)

# building a list of first_name and last name from fill name.

# full_name=['steve jobs','bill gates','joghn doe','tim cook']
# fname=[]
# lname=[]
# for i in full_name:
#     fname.append(i.split()[0])
#     lname.append(i.split()[1])
# print(fname)
# print(lname)
# comprehnsion way.
# print([name.split()[0]for i in ])






# wapt  list of even numbers 1 to 20.
# print([i for i in range(1,20)if i%2==0])

# wapt a list of pallindrome from given list.
# names=['steve','eve','john','anna','stella','bob']
# print([name for name in names if name==name[::-1]])

# wapt filtering out those names which are less than 6 characters.

# names=['apple','google','yahoo','gmail','instagram']
# print([name for name in names if len(name)<6])
# wapt filtering all the lang which starts with 'p'
names=['python','google','yahoo','facebook','help','php']
filterd=[chr for chr in names if chr.startswith('p')]
print(filterd)

wapt 
# it is only use for mutable collectins. i.e list,dict,set