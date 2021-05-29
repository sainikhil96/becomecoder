import math
l,b=map(float,input().split())
area=l*b
peri=2*(l+b)
dia=math.sqrt(pow(l,2)+pow(b,2))
print("%.2f"%area,end=" ")
print("%.2f"%peri,end=" ")
print("%.2f"%dia,end=" ")
