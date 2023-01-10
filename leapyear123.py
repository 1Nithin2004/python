#for leap year
year=float(input("enter a year:"))
if(year==0):
    print("false")
elif (year<0):
    print("false")
elif(year%400==0) and (year%100==0):
    print("is a leap year")
elif(year%4==0) and (year%100!=0):
    print("is a leap year")
else:
    print("is not a leap year")
    
