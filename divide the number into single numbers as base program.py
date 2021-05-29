"""
num=int(input())
while True:
    r=num%10
    num=num//10
    print(r,num)
    if num==0:
        break
"""

"""
num=int(input())
c=0
while num:
    r=num%10
    num=num//10
    c+=1
print(c)
"""


num=int(input("enter number:"))
count=0
while(num>0):
    r=num%10
    num=num//10
    count=count+1
    print(count)
