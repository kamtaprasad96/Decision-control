# write a python script to check whether a given quadratic equation has two real & 
# distinct roots, real & equal roots or imaginary roots

print("enter three number :")
a=int(input())
b=int(input())
c=int(input())
d=b*b-4*a*c
if d>0:
    print('real & distinct roots')
elif d==0:
    print('real & equal roots')
else:
    print('imaginary roots')