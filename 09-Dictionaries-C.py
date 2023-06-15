counts = dict()
#   we create a dictionary counting the words in a text
line = input ('Enter a line of text: ')
#   we ask the user to input a line of text and then store it in line
words = line.split()
#   we use the split function on the line that the user input and then store it inside of words
print ('Words:', words)
print ('Counting...')

# formula to count the histogram 
for word in words:
    counts[word] = counts.get(word,0) + 1
print ('Counts', counts)

# we create a dictionary
dict = {'gram': 1, 'kilo': 1000, 'dekagram': 10}

#and we can use functions to get things out of the dictionary

print(dict.keys())
#^this one prints all the keys in a dict

print(dict.values())

for aaa,bbb in dict.items() :
    print (aaa,bbb)