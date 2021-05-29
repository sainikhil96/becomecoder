num=int(input())
rev=0
l=num%10
c=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    c+=1
rev=rev%pow(10,c-1)
rev=rev//10
rev=rev*10+1
rev=r*pow(10,c-1)+rev
print(rev)
"""
m=temp%pow(10,c-2)
f=r
rev=0
while m:
    r=m%10
    m=m//10
    rev=rev*10+r
rev=rev*10+1
rev=rev%pow(10,c-1)
rev=r*pow(10,c-1)+rev
print(rev)
"""
