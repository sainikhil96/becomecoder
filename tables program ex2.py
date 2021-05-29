"""
num,r=map(int,input().split())
for i in range(1,21): 
    print(num,"X",i,"=",num*i)
    if i==r:
        break
    i+=1
"""

"""
num,r1,r2=map(int,input().split())
while r1<=r2:
    print(num,"X",i,"=",num*i)
    r1+=1
"""



"""
num,r1,r2=map(int,input().split())
inc=1
if r1>r2:
    inc=1
for i in range(r1,r2+inc,inc):
    print(num," X ",i," = ",num*i)
"""



"""
num,r1,r2=map(int,input().split())
for i in range(1,r2+1,1):
    if (num*i)%r1!=0:
        print(num," X ",i,"= ",num*i)
    else:
        continue
"""




