def lcm(a,b):
    m=max(a,b)
    for i in range(m,a*b+1):
        if i%a==0 and i%b==0:
            return i


a,b=map(int,input().split())
print(lcm(a,b))
