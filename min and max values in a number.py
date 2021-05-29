num=int(input())
m=num%10
n=num%10
while num:
    r=num%10
    num=num//10
    if r>n:
        n=r
    if r<m:
        m=r
print (m,n)

