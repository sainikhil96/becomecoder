num=int(input())
ec=0
oc=0
while num:
    r=num%10
    num=num//10
    if r%2:
        oc+=1
    else:
        ec+=1
if ec%2==0:
    print("EVEN")
elif oc%2==0:
    print("ODD")
elif ec%2 and oc%2==0:
    print("MIXED")
