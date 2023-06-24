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

test = aa("12 - 14")

print(test.counts)

#if index is even put it into numbers list, else put it into operators list
tmp = list()
operator = test.arranged[1:2]
fv = [float(i) for i in test.arranged[0:1]]
sv = [float(i) for i in test.arranged[2:3]]
print (type(fv))
print (type(sv))
if operator == ["+"]:
    print("its a plus")
    check = True
else:
    if operator == ["-"]:
        print("its a minus")
        check = True
    else:
        print("ERROR")
        check = False

if check == True:
    if operator == ["+"]:
        result = (fv + sv)
    else:
        result = (fv - sv)
print(result)

print(operator)



test2 = even(13)
print(test2.result)
print(even(13).result)

test3 = indent(1234)
print(test3.x)









x = "xxxx"
y = "yyy"
o = "o"
r = "rrrr"

print(len(x),len(y))

if len(x) == 4 or len(y) == 4:
    print("  ",x,"\n",
          o," ",y,"\n",
          "------","\n",
          "  ",r,
          sep="")
else:
    if len(x) == 3 or len(y) == 3:
        print("  ",x,y,sep="")
    else:
        if len(x) == 2 or len(y) == 2:
            print(  o,r,sep="")

