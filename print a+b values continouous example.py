"""
def gen_fib(n):
    a,b=0,1
    print(a,b,end=" ")
    i=3
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n=int(input())
gen_fib(n)

"""

"""
n=10

0 1 1 2 3 5 8 13 21 34.....
    a b c
"""



def gen_fib(n):
    if n==0:
        return
    if n==1:
        print(0)
        return
    a,b=0,1
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b 
        b=c   
n=int(input())
gen_fib(n)



"""

def gen_fib(n,a=0,b=1):
    if n==0:
        return
    if n==1:
        print(a)
        return
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n=int(input())
gen_fib(n)

"""
