
largest_so_far = -1
print('Before', largest_so_far)

list = [41,23,12,4,32,255]

for the_num in list :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print('largest so far:',largest_so_far,'current:',the_num)




print('After', largest_so_far)