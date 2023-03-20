#counting the amount of items in a list

tehe = 0
print('Before:',tehe)
for thing in [12,34,12,5,1,2,6,5,34,43] : 
    tehe = tehe + 1
    print(tehe, thing)
print('After:', tehe )

#summing up all the values in a list
sum = 0
print ('Before:', sum)
for num in [345,34,32,76,33,71,12,31] :
    sum = sum + num
    print (sum, num)
print('After:',sum)