
#lists are modulable
lotto = [12,23,1,4,2,21]
print (lotto[2])
lotto[2] = 5
print (lotto[2])

#ranges create an index for each of the values in a list

for i in range(len(lotto)) :
    number = lotto[i]
    print ('and the number we got is!',number)
