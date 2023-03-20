#first example while loop
n = 6
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print ('Finished.')

#second example. now with using a loop with a break conditional
#this program will wait for the user to type in 'done', if it doesnt find 'done', it will just output the input
while True : 
    line = input('> ')
    if line == 'done' :
        break
        #^ this makes it so that the loop "breaks", and the process can go on further and print out the last line
    print (line)
print ('Done!')