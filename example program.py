num=int(input())
even=0
odd=0
ec=1
oc=1
while num:
    r=num%10
    num=num//10
    if r%2:
        odd=odd*10+r
    else:
        even=even*10+r
print(even,odd)
