from array import *

val = array('i',[1,2,3,4,5,6,7,8,9,10])

print('\n')
for i in range(0,len(val)):
    print(val[i],end=" ")

print('\n')
for x in val:
    print(x,end=",")

print('\n')

print(val.typecode)

val.reverse()
for i in val:
    print(i,end=',')

