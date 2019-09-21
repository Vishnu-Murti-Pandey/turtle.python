year=int(input("enter a year"))
if(year%400==0):
    print("%d is leap year" %year)
elif(year%100==0):
    print("%d is not a leap year" %year)
elif(year%4==0):
    print("%d is a leap year" %year)
else:
    print("%d is not a leap year" %year)
    
