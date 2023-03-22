#06strings

string ='banana'

print(len(string))
#     ^length of string



#going through a string one by one
index = 0
while index < len(string) : 
    letter = string[index]
    print(index, letter)
    index = index + 1
#tedious way ^

#better way
for letter in string : 
        print(letter)

#counting letters in a word
word = 'banana'
count = 0
for let in word : 
    if let == 'a' : 
        count = count + 1
print(count)