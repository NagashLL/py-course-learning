import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
#here we use urllib to get the data without headers
counts = dict()
for line in fhand:
    words = line.decode().split()
                #we decode it here and split every line into the words list     
    for word in words:
        counts[word] = counts.get(word, 0) + 1
            #here we make a histogram



#and we use the ol formula to sort the histogram 
lst = list()
for key,val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse= True)

for (val,key) in lst:
    print(key,val)
