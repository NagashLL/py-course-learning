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

#taking an average of a list
zork = 0
# zork = count
treat = 0
# treat = sum
print('Before:',zork, treat)
for iteration in [12,34,12,5,1,2,6,5,34,43] : 
    zork = zork + 1
    treat = treat + iteration
    print(zork, treat, iteration)
print('After:', zork, treat , (treat / zork))

#continue at 4m 20s

#filtering a loop
print ('filtering a loop')

for value in [1,2,3,5,7,7,2,3,4] : 
    if value < 3 : 
        print (value , 'is smaller than 3')

#looking for a value, returning a boolean
found = False
print ('Before:', found)
for va in [345,34,32,76,33,71,12,31] :
    if va == 32 :
        found = True
    print (found, va)
print('After:',found)
#found the value, returns True