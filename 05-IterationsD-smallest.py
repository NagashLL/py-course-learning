#finding the smallest value
smallest = None
print('Before:', smallest)
for value in [-4,-16,0,5,2,5,3,1,8,9] : 
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print (smallest, value)
print ('After:', smallest)
