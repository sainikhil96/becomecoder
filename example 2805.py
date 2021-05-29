"""

num=int(input())
for i in range(num):
    for j in range(num):
        print("*",end="")
        print()

"""     

"""

num=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end="")
    print()

"""

"""
num=int(input())
for i in range(num):
    for j in range(num):
        print("*",end="")
        print()

"""

num=int(input())
for i in range(1,num+1):
    if i%2:
        x=1
        y=num
        d=1
    else:
        x=num
        y=1
        d=-1
    for j in range(x,y+d,d):
        print(j,end="")
    print()

    
