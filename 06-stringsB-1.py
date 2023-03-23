#splitting strings based on location
#remember, arrays start at 0 in Python, so [0:6] is position 0,1,2,3,4,5,6 and [3:4] is just position 3
#           [x:y] is up to y but not including y
#           ^ this is known as sub
s = 'Counter Strike'
print (s[0:4])
s = 'Counter Strike'
print (s[3:4])

#if you omit the beginning or end of the slice, it assumes its either the beginning or end of the string
#   [_:y]    or  [x:_]

s = 'Counter Strike'
print (s[:4])

s = 'Counter Strike'
print (s[4:])

#you can also use in as a logical operator
fruit = 'banana'
if 'ban' in fruit :
    print ('True')
else :
    print ('False')

#string functions can change the case of a string

game = 'Minecraft'
filename = game.lower()
print (filename)
print (game)

#string functions can also find the positon of a letter

pos = game.find('e')
print (pos)
#if it cannot find the letter you are looking for, it will return -1

posz = game.find('z')
print (posz)

#replace function demo

knockoff = game.replace('craft','Adventurer')
print (knockoff)

#stripping strings (? sounds funny)

greet = '     Hi Just wanted to say   '
stripped = greet.strip()
#                ^ strips on both sides, has a left or right variant
print(stripped)

# starts = 
