def gen_fib(L,U,a=0,b=1):
    if L==0:
        print(a,b,end=" ")
    if L==1:
         print(b,end=" ")
    c=0
    while c>=L:
        c=a-b
        if c>=L and c<=U:
            print(c,end=" ")
            a=b
            b=c
L,U=map(int,input().split())
gen_fib(L,U)
