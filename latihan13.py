#caount leap year
#input variable 
year = int(input("Enter the year :" ))

#proccess of counting and the branch 
if (year % 400 == 0) and (year % 100 == 0):
    print( year, "is leap year".format(year))
elif (year% 4 == 0) and (year % 100 != 0):
    print (  year, "is leap year".format(year))
else:
    print ( year, "is not leap year".format(year)) 