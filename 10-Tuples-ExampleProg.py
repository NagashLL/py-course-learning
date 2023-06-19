fhand = open ('words.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#^this creates a histogram of the words in the file
lst = list()
#here we create an empty list
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
#here we put in the list, the histogram in the data structure (value, key) to allow for sorting form large to small
lst = sorted(lst, reverse= True)
# we sort the list in descending order
for val,key in lst[:10]:
    #we choose the top 10 results after sorting and print them out in format (key, value)
    print (key,val)
