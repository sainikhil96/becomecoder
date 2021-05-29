"""s
a,b=map(int,input().split())
s=0
while True:
    if a%2:
        s=s+b
    if a==0:
        break
    a=a//2
    b=b*2
print(s)
    
"""

"""

a,b=map(int,input().split())
res=0
if a%2:
    res+=b
a=a//2
b=b*2
print(a,b,res)

"""


"""

def mul (a,b,res=0):
    while a:
        if a%2:
            res+=b
        a=a//2
        b=b*2
    return res

a,b=map(int,input().split())
res=mul(a,b)
print(res)

"""


