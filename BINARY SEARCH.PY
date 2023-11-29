def binary ():
    global x
    lo=0
    hi=len(x)-1
    print(hi)
    while(lo<=hi):
        mid=(lo+hi)//2
        if(z==x[mid]):
            return "exist"
        if(z>x[mid]):
            lo=mid+1
        if(z<x[mid]):
            hi=mid-1
        if(lo>hi):
           return  "not exist"
y=int(input("enter the range of your array"))       
import numpy as np
x=np.zeros(y,dtype="int16")
for i in range(y):
    a=int(input("enter the number"))
    x[i]=a
print(x)
z=int(input("enter your searching number"))
#f=0
v=binary()
print(v)