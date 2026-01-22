# normal way
# once return is executed inside function it will terminate further execution or it not allow the any other statement after  execution  ######
#  wapt to check given no is even or not if it even retrun true if is not retrun false .
def iseven(number):
    return number%2==0
print(iseven(5))
print(iseven(4))

# wapt to print list of even numbers between the range based on user enter limit as an arguments

def lst_even_numbers(start,end):
    return [numbers for numbers in range(start,end) if numbers%2==0]
print(lst_even_numbers(1,50))
print(lst_even_numbers(100,200))