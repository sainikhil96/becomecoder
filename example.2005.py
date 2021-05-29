def mul(a,b):
    if a==0:
        return 0
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return 0+mul(a//2,b*2)

a,b=map(int,input().split())
print(mul(a,b))




def fibi(a,b,d,num):
    if i>num:
        return
    if i==1:
        print(a,end=" ")
        i+=1
    if i==2:
        print(b,end=" ")
        i+=1
    if i<num:
        print(a+b,end=" ")
    fibi(b,a+b,d+1,num)

num=int(input())
a=0,b=1
i=1
fibi(0,1,1,num)
