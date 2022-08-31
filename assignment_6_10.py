# write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.


print('enter three numbers :')
a,b,c=int(input()),int(input()),int(input())
# print((a if a>c else c)if a>b else (b if b>c else c))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

