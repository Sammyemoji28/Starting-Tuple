
#creating a list

numbersL = [1,2,3,4]

#creating a tuple (packing)

numbersT = (1,2,3,4)
addressT = (12,"berrywood","cherrywood","applewood",123456)

#tuple (unpacking)

a,b,c,d,e = addressT
print(a)
print(b)
print(c)
print(d)
print(e)

#printing tuple

print(addressT)
print(addressT[2])

#printing letter from tuple

print(addressT[1])
print(addressT[1][5])

#printing all 1 by 1 in tuple, same line

for i in addressT:
    print(i)

for i in addressT:
    print(i,end=", ")

#creating new tuple

myTuple = 1,2,3,4,5

print(myTuple)

#nested tuple (list in tuple)

nestedT = ("hi",[1,2,6,4,7],(5,3,8,9,10))

print(nestedT[1][4])
print(nestedT[2][3])
    
#creating ANOTHER tuple

anotherT = (11,12,13,14,15,16,17,18,19,20)

#negative Indexing

print(anotherT[-5])
print(anotherT[-9])

#printing multiple numbers (include +1 more for last index number or number wont show)

print(anotherT[2:7])

#starting and begin. and going to end! dont add second num for end, begin. doesnt matter

print(anotherT[-8:])
print(anotherT[0:6])
print(anotherT)

