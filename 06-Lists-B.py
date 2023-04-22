#concatenating lists
a = [1,2,3,4]
b = [10,9,8,7]
c = a + b
print (c)

#splitting lists, values in a list are indexed in an array
# [x:y] up to y BUT NOT INCLUDING
print (a[1:3])


#making an empty list
stuff = list()

stuff.append(9)
stuff.append(12)
stuff.append('cars')
print(stuff)

#checking if something is in a list
if 9 in stuff :
    print (True)
else :
    print (False)

if 16 in stuff :
    print (True)
else :
    print (False)

#you can also do operations on a list
print(sum(c))