#dictionaries
dict = {}
#       ^curly brackets indicate a dictionary

dict['purse'] = 12
#here we add an item with the key purse, and a assign that a value of 12
print (dict)

#lets add some more items to the dictionary
dict['loaf'] = 31
dict['chicken'] = 7

print (dict)

#and we can change the items inside of a dictionary by accesing it via key, instead of position

dict['loaf'] = dict['loaf'] + 10

print (dict)


#histograms! the most common use for a dictionary

counts = {}
#^creates the counts dictionary, counting all the names and the number of times they appear
names = ['quincy','jill','gwen','james','bart','quincy']


for name in names :
    if name not in counts :
        #if the name doesnt exist in the dictionary, take the name as a key, put it in the dictionary and assign it a value of 1 occurence
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
        #if it does already exist, just increment the count of the name by 1
print(counts)


#there is also a much more straightforward way to do the same, using the .get function


counts2 = {}
for name in names :
    counts2[name] = counts2.get(name, 0) + 1
                    #it "gets"  a name(key), default sets a value of 0, and then we add 1 to it
print (counts2)

#same result, much more simple