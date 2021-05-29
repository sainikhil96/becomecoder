"""
def isarmstrong(num):
    temp=num
    dc=0
    while temp:
        temp=temp//10
        dc+=1
    #print(dc)
    res=0
    temp=num
    while temp:
        r=temp%10
        temp=temp//10
        res+=pow(r,dc)
    if num=res:
        return True
    return False

num=int(input())
print(isamstrong(num))

"""



def digitcount(num):
    dc=0
    while num:
        num=num//10
        dc+1
    return dc
def isarmstrong(num,dc):
    if num==0:
        return 0
    return pow(num%10,dc)+isarmstrong(num//10,dc)


num=int(input())
dc=digitcount(num)
print(num==isarmstrong(num,dc))
    
