import math

#input 
a = float(input("Enter the coeficient a : "))
b = float(input("Enter the coeficient b : ")) 
c = float(input("Enter the coeficient c : ")) 

#input proccess 
discriminant = b**2 - 4*a*c 

#brach of proccess of variable
#if more than 0
if discriminant > 0: 
    root1 = (-b + math.sqrt(discriminant)) / 2*a
    root2 = (-b - math.sqrt(discriminant)) / 2*a  
    print("Root 1 :", root1)
    print ("Root 2 : ", root2)
#if it is equal with zeor
elif discriminant == 0:
    root = -b/(2*a) 
    print ("Root : ", root)
#if it is other than 0 and more 0 
else:
    real_part = -b / (2*a)
    primary_part = math.sqrt(abs(discriminant)) / (2*a) 
    print("Root 1 :", real_part + primary_part)
    print("Root 1 :", real_part - primary_part)