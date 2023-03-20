def greet ():
    return ('Hello')
    #return gives a value instead of executing a command or printing something out. It can be used further on in 
    #return also ends the function and puts the return value into memory
print (greet(), "World")
print (greet(), "James")

def custom (x):
    if x == 1 : 
        return ('True')
        # this was true so it ends the function and gives true as a result
    elif x == 0 :
        return ('False')
    return ('Mystery???!!!')

print (custom(1))
# calls for the function with argument 1 and prints out the value

def sum (a , b) : 
    added = a + b
    return (added)

print (sum(1, 4)) 