fhand = open('example.txt')
print (fhand)

# \n is a newline character or break

#prints out all the lines in file

#       for line in fhand :
#           print (line)

#counts out the number of lines in a file
count = 0
for line in fhand : 
    count = count + 1
print ('Line count:', count)
print (type(count))

# gives the length of the object read from the text file
ghand = open('example.txt')
inp = ghand.read()
#       ^ the object is a series of comma separated values 
print (len(inp))
#          ^ gives us the length of the object (how many values there are)

# goes through a file looking for a line
jhand = open('example.txt')
for line in jhand : 
    if line.startswith('2') :
        print (line)
    else :
            print('none')
# the output of this is 
#   none
#   2 \n (newline from the text file)
#   \n (newline added by python) -> there is double the amount of space necessary
#   none

#fixed file search with whitespace removed
ahand = open('example.txt')
for line in ahand : 
    line = line.rstrip()
    if line.startswith('2') :
        print (line)
    else :
            print('none')