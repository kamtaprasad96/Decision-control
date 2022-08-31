# write a python script to check whether a given year is a leap year or not

year=int(input('enter a year '))
if year%100==0 or year%4==0:
    print('year is leap year') 
else:
    print('year is not leap year')