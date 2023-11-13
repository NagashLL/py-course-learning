class aa:
    raw = ""
    arranged = ()
    counts = {}
    def __init__(self,inpt):
        self.raw = inpt
        self.arranged = inpt.split()
        print(self.arranged)
        for item in self.arranged:
            self.counts [item] = self.arranged.index(item)
        print(self.counts)    
class even:
    number = int()
    result = bool
    def __init__(self,checked):
        self.number = checked
        if type(int(self.number/2)) is int and int(self.number/2) == self.number /2:
            self.result = True
        else:
            self.result = False

class indent:
    x = str()
    def __init__(self,take):
            self.x = take
            self.x = str(self.x)
            if len(self.x) == 5:
                self.x = " " + self.x
            else:    
                if len(self.x) == 4:
                    self.x = "  " + self.x
                    print(self.x)
                else:
                    if len(self.x) == 3:
                        self.x = "   " + self.x
                    else:
                        if len(self.x) == 2:
                            self.x = "    " + self.x
                        else:
                            self.x = "     " + self.x

#this class adds the amount of spaces based on the desired amount
class spacedout:
    todo = int()
    def __init__(self,y):
        self.todo = y
     #   if self.todo = 6:

test = aa("111 + 999")

print(test.counts)

#if index is even put it into numbers list, else put it into operators list

operator = [str(i) for i in test.arranged[1:2]]
operator = str(operator)

fv = [float(i) for i in test.arranged[0:1]]
fv = float(str(fv).strip("[]"))


sv = [float(i) for i in test.arranged[2:3]]
sv = float(str(sv).strip("[]"))

if ('+' in operator):
    print("its a plus")
    check = True
else:
    if ('-' in operator):
        print("its a minus")
        check = True
    else:
        print("ERROR")
        check = False


if check == True:
    if ('+' in operator):
        result = (fv + sv)
    else:
        result = (fv - sv)
print(result)





test2 = even(13)
print(test2.result)
print(even(13).result)

test3 = indent(123)








r = "rrrr"

fsv = indent(int(fv))
ssv = str(operator.strip("[]'")) + str(int(sv))
resulted = indent(str(int(result)))

mood = [len(str(int(fv))),len(str(int(sv))),len(str(int(result)))]

print(mood)
desired = max(mood)

print(desired)

#based on desired, lstrip fsv , ssv and resulted

done = [str(fsv.x),"\n", ssv,"\n","------","\n",resulted.x]
did = ""
for v in done:
    did = did + v

print(did)