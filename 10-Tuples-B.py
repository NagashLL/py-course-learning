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
#we create a new data structure where the values are first, and then keys


print ('unsorted:', tmp)
#here we just showcase the unsorted temp list


tmp = sorted(tmp, reverse= True)
#we use the sorted function to sort the list by VALUES going BIG to SMALL (because reverse = True)

print('sorted:',tmp)
#here we just show the resulted, sorted list

import os
print(os.getcwd())
