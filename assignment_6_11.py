# write a python script to take the month value in numeric format and display the 
# number of days in it

month=int(input('enter a month:'))
if month in (1,3,5,7,8,10,12):
    print("31")
elif month in (4,6,9,11):
    print("30")
else:
    print("28/29")
