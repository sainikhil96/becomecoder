"""
def seq(n):
    if n%2:
        return 3*n+1
    return n//2

n=int(input())
print(n,end=" ")
while(n:=seq(n)):
    print(n,end=" ")
    if n==1:
        break

"""
    
def seq(n):
    if n==1:
        print(n,end=" ")
        return
    print(n,end=" ")
    if n%2:
        seq(3*n+1)
    else:
        seq(n//2)


n=int(input())
seq(n)
