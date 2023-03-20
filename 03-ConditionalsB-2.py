x = 'HelloWorld'
try:
    intx = int(x)
    # try this, if it doesnt work a.k.a throws an error, do except
except:
    intx = 10
print ('i found value x =',intx)



y = 123
try:
    inty = int(y)
    # this will succeed, so try is executed

except:
    inty = 20
    # except is skipped here since try worked

print ('i found value y =', inty)



val = 'string'
try :
    print('I found a string')
    s2i = int(val)
    print('finished converting to integer')

    # except is the fallback route
except : 
    s2i = -1
    print('fallback route, couldnt find string')
    # if it doesnt work out do fallback 
print ('result', s2i)