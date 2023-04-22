#creates an empty list

stuff = list()

#we append items to the list

stuff.append('book')
stuff.append(99)

#we can check whether an item is in a list using the In operator
#this results in a t/f result
print (99 in stuff)

#when we sort lists, we change the list itself

letters = ['c', 'a', 'b']
letters.sort()
print(letters[0])

#there is a lot of functions related to numbers in a list
nums = [3, 23, 21, 54, 10, 21, 8, 5, 9]

print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums)) #sum

print(sum(nums) / len(nums)) #average

