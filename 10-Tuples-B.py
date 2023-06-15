d = {'a':10, 'b': 1, 'c':22}
#we create a dictionary
print(d.items())
#here we just get the dictionary as a list of tuples
dsort = sorted(d.items())
#we use the sorted function to sort the list of tuples a->z
print(dsort)




#we create a temporary list
tmp = list()

for k, v in d.items():
    tmp.append( (v, k))

print ('unsorted:', tmp)

tmp 
